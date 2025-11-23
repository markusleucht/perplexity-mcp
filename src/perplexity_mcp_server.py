#!/usr/bin/env /opt/homebrew/bin/python3.11
"""
Official MCP server for Perplexity AI integration with Claude Code.
Uses the official Anthropic MCP SDK.
"""

import os
from typing import Optional
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

# Load environment variables
load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("PERPLEXITY_API_KEY not set in .env file")

# Initialize Perplexity client
client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

# Initialize FastMCP server
mcp = FastMCP("Perplexity Search")


class SearchRequest(BaseModel):
    """Request parameters for Perplexity search."""
    query: str = Field(description="The search query (any language, auto-detected)")
    search_type: str = Field(
        default="auto",
        description="Search type: 'pro' (deep research), 'auto' (balanced, recommended), 'fast' (quick results)"
    )
    max_tokens: int = Field(
        default=1024,
        ge=100,
        le=4000,
        description="Maximum tokens in response (100-4000)"
    )
    sources: list[str] = Field(
        default=["web"],
        description="Sources to search: 'web', 'social', 'scholar' - can combine multiple"
    )
    language: str = Field(
        default="en",
        description="Response language: 'en' (English), 'de' (Deutsch), 'es', 'fr', 'it'"
    )
    save_to_file: Optional[str] = Field(
        default=None,
        description="Optional file path to save markdown report (e.g., 'report.md')"
    )


class SocialSearchRequest(BaseModel):
    """Request parameters for social media search."""
    query: str = Field(description="Search query for social media/forums")
    max_tokens: int = Field(default=1024, ge=100, le=4000)
    save_to_file: Optional[str] = Field(default=None)


def format_to_markdown(query: str, content: str, citations: list, search_type: str, search_focus: str = None) -> str:
    """Format search results as professional markdown report."""
    today = datetime.now().strftime("%d. %B %Y")

    md = content + "\n\n"

    if citations:
        md += "## Quellen\n\n"
        for i, citation in enumerate(citations, 1):
            md += f"{i}. {citation}\n"

    md += "\n---\n\n"
    md += f"*Recherchiert: {today}*\n"
    method = "mit Fokus auf soziale Medien und Fachforen" if search_focus == "social" else "auf Web-Quellen"
    model = "sonar-pro" if search_type == "pro" else "sonar"
    md += f"*Methode: Perplexity {'Pro' if search_type == 'pro' else ''} Search {method} ({model})*\n"
    md += f"*Anfrage: {query}*\n"

    return md


@mcp.tool()
def perplexity_search(request: SearchRequest) -> dict:
    """
    Perform Perplexity Search with web crawling, real-time data, and verified sources.

    Returns professional markdown reports with 15-20 source citations.
    Supports web, social media, and academic sources.

    Cost: ~$0.005-0.01 per search (auto/fast), ~$0.01-0.02 per search (pro)
    """
    try:
        # Language mapping for system instruction
        language_map = {
            "de": "Deutsch (German)",
            "es": "Español (Spanish)",
            "fr": "Français (French)",
            "it": "Italiano (Italian)",
            "en": "English",
        }
        lang_name = language_map.get(request.language, "English")

        # Build system message with research guidelines
        system_message = f"""You are a precision research assistant.

Requirements:
- Use **specific data with year** (no generic statements)
- Always add **context**: change over time + comparison to relevant benchmarks
- If no reliable sources: clearly say so (no guessing)
- Structure:
  1) **Key facts** (2–3 sentences, with numbers)
  2) **Data points** (bullets, incl. year)
  3) **Brief interpretation**
  4) **Sources** (institution + year)

Provide your response in {lang_name}."""

        # Select model based on search type
        model = "sonar-pro" if request.search_type == "pro" else "sonar"

        # Build request
        request_kwargs = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.query}
            ],
            "max_tokens": request.max_tokens,
            "stream": False,
            "web_search_options": {"search_type": request.search_type},
        }

        # Add sources if specified
        if request.sources:
            request_kwargs["extra_body"] = {"sources": request.sources}

        # Perform search
        response = client.chat.completions.create(**request_kwargs)
        content = response.choices[0].message.content

        # Extract citations
        response_dict = response.model_dump()
        citations = []

        if 'citations' in response_dict and response_dict['citations']:
            citations = response_dict['citations']

        if 'search_results' in response_dict and response_dict['search_results']:
            search_results = response_dict['search_results']
            if not citations:
                citations = [result.get('url') for result in search_results if result.get('url')]

        # Format as markdown
        markdown = format_to_markdown(request.query, content, citations, request.search_type)

        result = {
            "success": True,
            "content": content,
            "citations": citations,
            "search_type": request.search_type,
            "sources": request.sources,
            "language": request.language,
            "markdown": markdown,
        }

        # Save to file if requested
        if request.save_to_file:
            try:
                # Default to reports/ directory
                filepath = request.save_to_file
                if "/" not in filepath:
                    filepath = f"reports/{filepath}"

                os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
                with open(filepath, "w") as f:
                    f.write(markdown)
                result["file_saved"] = filepath
            except Exception as e:
                result["file_error"] = str(e)

        return result

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "content": None,
            "citations": [],
        }


@mcp.tool()
def perplexity_social(request: SocialSearchRequest) -> dict:
    """
    Search social media and expert forums (Twitter/X, Reddit, forums) with Perplexity.

    Returns professional markdown report with verified source citations.
    """
    try:
        system_message = """You are a precision research assistant.

Requirements:
- Use **specific data with year** (no generic statements)
- Always add **context**: change over time + comparison to relevant benchmarks
- If no reliable sources: clearly say so (no guessing)
- Structure:
  1) **Key facts** (2–3 sentences, with numbers)
  2) **Data points** (bullets, incl. year)
  3) **Brief interpretation**
  4) **Sources** (institution + year)

Provide your response in English."""

        # Social search uses sonar-pro with social sources
        response = client.chat.completions.create(
            model="sonar-pro",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": request.query}
            ],
            max_tokens=request.max_tokens,
            stream=False,
            web_search_options={"search_type": "pro"},
            extra_body={"sources": ["social"]},
        )

        content = response.choices[0].message.content

        # Extract citations
        response_dict = response.model_dump()
        citations = []

        if 'citations' in response_dict and response_dict['citations']:
            citations = response_dict['citations']

        if 'search_results' in response_dict and response_dict['search_results']:
            search_results = response_dict['search_results']
            if not citations:
                citations = [result.get('url') for result in search_results if result.get('url')]

        # Format as markdown
        markdown = format_to_markdown(request.query, content, citations, "pro", "social")

        result = {
            "success": True,
            "content": content,
            "citations": citations,
            "search_focus": "social",
            "markdown": markdown,
        }

        # Save to file if requested
        if request.save_to_file:
            try:
                filepath = request.save_to_file
                if "/" not in filepath:
                    filepath = f"reports/{filepath}"

                os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
                with open(filepath, "w") as f:
                    f.write(markdown)
                result["file_saved"] = filepath
            except Exception as e:
                result["file_error"] = str(e)

        return result

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "content": None,
            "citations": [],
        }


if __name__ == "__main__":
    # Run the MCP server on stdio
    mcp.run()
