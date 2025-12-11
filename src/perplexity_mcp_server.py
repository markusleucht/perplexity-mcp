#!/usr/bin/env python3
"""
Unified Perplexity MCP Server for Claude Code.

Tools:
- perplexity_pro: Pro Search with sonar-pro (200K context) - quick research, social, academic
- perplexity_deep: Deep Research with sonar-deep-research - exhaustive analysis
"""

import os
import json
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, ConfigDict
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

from .prompt_enrichment import enrich_query, is_pharma_query, get_pharma_system_context

# Load environment variables
load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("PERPLEXITY_API_KEY not set in .env file")

# Initialize Perplexity client
client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

# Initialize FastMCP server
mcp = FastMCP("Perplexity Research")


# ============================================================================
# SYSTEM PROMPTS
# ============================================================================

def get_pro_system_prompt(language: str = "de") -> str:
    """Get system prompt for Pro Search with specified output language."""
    language_map = {
        "de": "Deutsch",
        "en": "English",
        "es": "Español",
        "fr": "Français",
        "it": "Italiano",
    }
    lang_name = language_map.get(language, "Deutsch")

    return f"""Du bist ein praeziser Recherche-Assistent.

Anforderungen:
- Nutze **spezifische Daten mit Jahreszahl** (keine generischen Aussagen)
- Fuege immer **Kontext** hinzu: Veraenderung ueber Zeit + Vergleich mit Benchmarks
- Wenn keine zuverlaessigen Quellen: klar sagen (nicht raten)
- Struktur:
  1) **Kernfakten** (2-3 Saetze, mit Zahlen)
  2) **Datenpunkte** (Aufzaehlung, inkl. Jahr)
  3) **Kurze Interpretation**
  4) **Quellen** (Institution + Jahr)

Antworte auf {lang_name}."""


DEEP_RESEARCH_SYSTEM_PROMPT = """Du bist ein Experte fuer Marktforschung und Analyse.

Anforderungen:
- Liefere evidenzbasierte Erkenntnisse mit konkreten Daten und Jahreszahlen
- Zitiere Quellen im Text natuerlich (z.B. "Laut RKI-Daten 2024...")
- Benenne Datenluecken klar, anstatt zu spekulieren
- Schreibe ausfuehrlich und vollstaendig - keine Zusammenfassungen
- Vermeide uebermassige Tabellen - bevorzuge Fliesstext mit Aufzaehlungen

Praesentiere die Ergebnisse in deinem natuerlichen Erzaehlstil.
Erzwinge keine starren Strukturen oder repetitive Formate.

Antworte auf Deutsch."""


# ============================================================================
# REQUEST MODELS
# ============================================================================

class ProSearchRequest(BaseModel):
    """Request parameters for Pro Search."""
    model_config = ConfigDict(str_strip_whitespace=True)

    query: str = Field(
        ...,
        description="Search query (any language). Searches global sources.",
        min_length=3,
        max_length=10000
    )
    sources: List[str] = Field(
        default=["web"],
        description="Sources: 'web' (general), 'social' (Twitter/Reddit/forums), 'scholar' (academic). Can combine."
    )
    search_recency_filter: Optional[str] = Field(
        default=None,
        description="Recency filter: 'day', 'week', 'month', 'year'. None = all time (5yr default via enrichment)."
    )
    response_language: str = Field(
        default="de",
        description="Output language: 'de' (German), 'en', 'es', 'fr', 'it'. Does NOT limit search sources."
    )
    report_name: Optional[str] = Field(
        default=None,
        description="Save report to docs/reports/{date}_{name}/. E.g., 'bimzelx_analysis'"
    )


class DeepResearchRequest(BaseModel):
    """Request parameters for Deep Research."""
    model_config = ConfigDict(str_strip_whitespace=True)

    query: str = Field(
        ...,
        description="Research query. Pharma context auto-detected and enriched.",
        min_length=5,
        max_length=10000
    )
    context_hint: Optional[str] = Field(
        default=None,
        description="Context hint: 'pharma', 'market', 'tech'. Auto-detected if omitted."
    )
    skip_enrichment: bool = Field(
        default=False,
        description="If True, send raw query without search optimization."
    )
    report_name: Optional[str] = Field(
        default=None,
        description="Save report to docs/reports/{date}_{name}/. E.g., 'ozempic_market_research'"
    )


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def save_report(report_name: str, content: str, citations: list, search_results: list) -> str:
    """
    Save raw Perplexity output to docs/reports/{ddMMYY}_{report_name}/.

    Creates 3 files:
    - content.md: Raw response text
    - citations.json: URL array
    - search_results.json: Rich source data (title, URL, date)

    Returns folder path.
    """
    date_prefix = datetime.now().strftime("%d%m%y")
    folder = f"docs/reports/{date_prefix}_{report_name}"
    os.makedirs(folder, exist_ok=True)

    # content.md - raw markdown
    with open(f"{folder}/content.md", "w", encoding="utf-8") as f:
        f.write(content)

    # citations.json - URL array
    with open(f"{folder}/citations.json", "w", encoding="utf-8") as f:
        json.dump(citations, f, indent=2, ensure_ascii=False)

    # search_results.json - rich source data
    with open(f"{folder}/search_results.json", "w", encoding="utf-8") as f:
        json.dump(search_results, f, indent=2, ensure_ascii=False)

    return folder


# ============================================================================
# TOOLS
# ============================================================================

@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "openWorldHint": True,
        "idempotentHint": True,
    }
)
def perplexity_pro(request: ProSearchRequest) -> dict:
    """
    Pro Search with sonar-pro model (200K context).

    Features:
    - search_context_size: high (maximum search depth)
    - Configurable sources: web, social, scholar
    - Configurable recency filter
    - German output by default (searches global sources)

    Use for:
    - Quick research tasks
    - Current events and news
    - Social media sentiment (sources=["social"])
    - Academic papers (sources=["scholar"])
    - Competitive intelligence snapshots

    For exhaustive research requiring deep analysis, use perplexity_deep instead.
    """
    try:
        # Build system prompt with response language
        system_content = get_pro_system_prompt(request.response_language)

        # Add pharma context if detected
        if is_pharma_query(request.query):
            system_content += "\n\n" + get_pharma_system_context()

        # Build API request - NO max_tokens limit
        request_kwargs = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": request.query}
            ],
            "stream": False,
            "web_search_options": {
                "search_context_size": "high"
            },
        }

        # Add sources
        if request.sources:
            request_kwargs["extra_body"] = {"sources": request.sources}

        # Add recency filter if specified
        if request.search_recency_filter:
            request_kwargs["web_search_options"]["search_recency_filter"] = request.search_recency_filter

        # Perform search
        response = client.chat.completions.create(**request_kwargs)
        content = response.choices[0].message.content

        # Extract citations and search_results (raw)
        response_dict = response.model_dump()
        citations = response_dict.get("citations", [])
        search_results = response_dict.get("search_results", [])

        # Build result
        result = {
            "success": True,
            "content": content,
            "citations": citations,
            "search_results": search_results,
            "metadata": {
                "model": "sonar-pro",
                "sources": request.sources,
                "response_language": request.response_language,
                "search_context_size": "high",
                "timestamp": datetime.now().isoformat(),
            }
        }

        # Save report if requested
        if request.report_name:
            try:
                folder = save_report(
                    report_name=request.report_name,
                    content=content,
                    citations=citations,
                    search_results=search_results
                )
                result["report_saved"] = folder
            except Exception as e:
                result["report_error"] = str(e)

        return result

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "content": None,
            "citations": [],
            "search_results": [],
        }


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "openWorldHint": True,
        "idempotentHint": True,
    }
)
def perplexity_deep(request: DeepResearchRequest) -> dict:
    """
    Deep Research with sonar-deep-research model.

    Maximum quality settings:
    - reasoning_effort: high
    - search_context_size: high
    - NO token limits (full output)
    - Raw, unaltered Perplexity response

    Features:
    - Auto-detects pharma queries and applies enrichment
    - Default pharma marketing agency context (Berlin)
    - 5-year default timeframe via prompt enrichment
    - Comprehensive source citations

    Use for:
    - Comprehensive market research
    - Detailed product analysis
    - In-depth competitive intelligence
    - Any topic requiring exhaustive research

    For quick searches, use perplexity_pro instead.
    """
    try:
        # Enrich query following Perplexity best practices
        enriched_query, enrichment_meta = enrich_query(
            query=request.query,
            context_hint=request.context_hint,
            skip_enrichment=request.skip_enrichment
        )

        # Build system prompt
        system_content = DEEP_RESEARCH_SYSTEM_PROMPT

        # Add pharma context if detected
        if is_pharma_query(request.query) or request.context_hint == "pharma":
            system_content += "\n\n" + get_pharma_system_context()

        # API call with MAXIMUM QUALITY settings
        # NO max_tokens - unlimited output
        response = client.chat.completions.create(
            model="sonar-deep-research",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": enriched_query}
            ],
            stream=False,
            reasoning_effort="high",
            web_search_options={
                "search_context_size": "high"
            },
        )

        # Extract content (RAW, UNALTERED)
        content = response.choices[0].message.content

        # Extract citations and search_results (raw)
        response_dict = response.model_dump()
        citations = response_dict.get("citations", [])
        search_results = response_dict.get("search_results", [])

        # Build result
        result = {
            "success": True,
            "content": content,
            "citations": citations,
            "search_results": search_results,
            "metadata": {
                "model": "sonar-deep-research",
                "reasoning_effort": "high",
                "search_context_size": "high",
                "enriched_query": enriched_query if not request.skip_enrichment else None,
                "enrichment_applied": enrichment_meta.get("enriched", False),
                "entities_detected": enrichment_meta.get("entities_detected", {}),
                "context_applied": enrichment_meta.get("context_applied", []),
                "timestamp": datetime.now().isoformat(),
            }
        }

        # Save report if requested
        if request.report_name:
            try:
                folder = save_report(
                    report_name=request.report_name,
                    content=content,
                    citations=citations,
                    search_results=search_results
                )
                result["report_saved"] = folder
            except Exception as e:
                result["report_error"] = str(e)

        return result

    except Exception as e:
        return {
            "success": False,
            "error": f"Deep research failed: {str(e)}",
            "content": None,
            "citations": [],
            "search_results": [],
        }


if __name__ == "__main__":
    mcp.run()
