#!/usr/bin/env python3
"""
Lean MCP server for Perplexity AI with Pro Search and social-focused capabilities.
"""

import os
import sys
import json
import subprocess
from typing import Any, Dict

def ensure_dependencies():
    """Ensure required packages are installed, install if missing."""
    required_packages = {
        'openai': 'openai>=1.0.0',
        'dotenv': 'python-dotenv>=0.19.0'
    }

    missing = []
    for package_import, package_install in required_packages.items():
        try:
            __import__(package_import)
        except ImportError:
            missing.append(package_install)

    if missing:
        print(f"📦 Installing missing dependencies: {', '.join(missing)}")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '--user', '--quiet'
            ] + missing)
            print("✓ Dependencies installed successfully")
            # Reload the modules
            import importlib
            importlib.invalidate_caches()
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            print("   Please run: pip install --user openai python-dotenv")
            return False
    return True

# Ensure dependencies are installed
if not ensure_dependencies():
    sys.exit(1)

# Now import the packages
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("PERPLEXITY_API_KEY not set in .env file")

client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")
HAS_OPENAI = True


def format_to_markdown(
    query: str,
    content: str,
    citations: list,
    search_type: str = "pro",
    search_focus: str = None,
) -> str:
    """
    Format search results as professional markdown report.

    Args:
        query: The original query
        content: The search result content
        citations: List of citation URLs
        search_type: Type of search performed
        search_focus: Focus type (e.g., "social")

    Returns:
        Formatted markdown string
    """
    from datetime import datetime

    # Get current date in German format
    today = datetime.now().strftime("%d. %B %Y")

    md = content + "\n\n"

    if citations:
        md += "## Quellen\n\n"
        for i, citation in enumerate(citations, 1):
            md += f"{i}. {citation}\n"

    # Footer with metadata
    md += "\n---\n\n"
    md += f"*Recherchiert: {today}*\n"
    md += f"*Methode: Perplexity Pro Search {'mit Fokus auf soziale Medien und Fachforen' if search_focus == 'social' else 'auf Web-Quellen'} (sonar-pro)*\n"
    md += f"*Anfrage: {query}*\n"

    return md


def perplexity_search(
    query: str,
    search_type: str = "pro",
    max_tokens: int = 1024,
    format_as: str = "dict",
    save_to_file: str = None,
    sources: list = None,
    language: str = "en",
) -> Dict[str, Any]:
    """
    Perform a Pro Search on Perplexity with streaming support.

    Args:
        query: The search query
        search_type: "pro", "auto", or "fast" (default: "pro")
        max_tokens: Maximum tokens in response (default: 1024)
        format_as: "dict" (JSON), "markdown" (MD), or "both" (default: "dict")
        save_to_file: Optional file path to save markdown output (e.g., "/path/to/file.md")
        sources: List of sources to search. Options: ["web"], ["social"], ["scholar"],
                or combinations like ["web", "social"]. Default: ["web"]
        language: Response language (e.g., "en" for English, "de" for German, "es" for Spanish).
                 Default: "en"

    Returns:
        dict with 'content', 'markdown', 'citations' and metadata
    """
    if search_type not in ["pro", "auto", "fast"]:
        search_type = "pro"

    # Default to web search if no sources specified
    if sources is None:
        sources = ["web"]

    # Language mapping for system instruction
    language_map = {
        "de": "Deutsch (German)",
        "es": "Español (Spanish)",
        "fr": "Français (French)",
        "it": "Italiano (Italian)",
        "en": "English",
    }
    lang_name = language_map.get(language, "English")

    try:
        citations = []
        search_results = []

        # Build system message with research guidelines and language instruction
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

        # Build request kwargs
        request_kwargs = {
            "model": "sonar-pro",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": query}
            ],
            "max_tokens": max_tokens,
            "stream": False,
            "web_search_options": {"search_type": search_type},
        }

        # Add sources if specified
        if sources:
            request_kwargs["extra_body"] = {"sources": sources}

        # Pro Search with non-streaming to capture complete search_results
        # search_results are only available in non-streaming mode
        response = client.chat.completions.create(**request_kwargs)

        content = response.choices[0].message.content

        # Extract citations from response
        # The response object contains both 'citations' and 'search_results'
        response_dict = response.model_dump()

        # Get citations list (URLs only)
        if 'citations' in response_dict and response_dict['citations']:
            citations = response_dict['citations']

        # Also try search_results for more detailed info
        if 'search_results' in response_dict and response_dict['search_results']:
            search_results = response_dict['search_results']
            # If we didn't get citations, extract URLs from search_results
            if not citations:
                citations = [result.get('url') for result in search_results if result.get('url')]

        markdown = format_to_markdown(query, content, citations, search_type)

        result = {
            "success": True,
            "content": content,
            "citations": citations,
            "search_type": search_type,
            "sources": sources,
            "language": language,
            "markdown": markdown,
        }

        if save_to_file:
            try:
                # Default to reports/ directory if no path specified
                if "/" not in save_to_file:
                    save_to_file = f"reports/{save_to_file}"

                os.makedirs(os.path.dirname(save_to_file) or ".", exist_ok=True)
                with open(save_to_file, "w") as f:
                    f.write(markdown)
                result["file_saved"] = save_to_file
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


def perplexity_social(
    query: str,
    max_tokens: int = 1024,
    save_to_file: str = None,
) -> Dict[str, Any]:
    """
    Perform a social-focused search (X/Twitter, Reddit, etc.).

    Args:
        query: The search query
        max_tokens: Maximum tokens in response (default: 1024)
        save_to_file: Optional file path to save markdown output (e.g., "/path/to/file.md")

    Returns:
        dict with 'content', 'markdown', 'citations' and metadata
    """
    try:
        citations = []
        search_results = []

        # Build system message with research guidelines
        system_message = """You are a precision research assistant analyzing social media discussions.

Requirements:
- Use **specific data with year** (no generic statements)
- Always add **context**: change over time + comparison to relevant benchmarks
- If no reliable sources: clearly say so (no guessing)
- Structure:
  1) **Key facts** (2–3 sentences, with numbers)
  2) **Data points** (bullets, incl. year)
  3) **Brief interpretation**
  4) **Sources** (institution + year)"""

        # Pro Search with social sources - use non-streaming to get search_results
        response = client.chat.completions.create(
            model="sonar-pro",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": query}
            ],
            max_tokens=max_tokens,
            stream=False,
            extra_body={"sources": ["social"]},
            web_search_options={"search_type": "pro"},
        )

        content = response.choices[0].message.content

        # Extract citations from response
        response_dict = response.model_dump()

        # Get citations list (URLs only)
        if 'citations' in response_dict and response_dict['citations']:
            citations = response_dict['citations']

        # Also try search_results for more detailed info
        if 'search_results' in response_dict and response_dict['search_results']:
            search_results = response_dict['search_results']
            # If we didn't get citations, extract URLs from search_results
            if not citations:
                citations = [result.get('url') for result in search_results if result.get('url')]

        markdown = format_to_markdown(query, content, citations, "pro", "social")

        result = {
            "success": True,
            "content": content,
            "citations": citations,
            "search_focus": "social",
            "markdown": markdown,
        }

        if save_to_file:
            try:
                # Default to reports/ directory if no path specified
                if "/" not in save_to_file:
                    save_to_file = f"reports/{save_to_file}"

                os.makedirs(os.path.dirname(save_to_file) or ".", exist_ok=True)
                with open(save_to_file, "w") as f:
                    f.write(markdown)
                result["file_saved"] = save_to_file
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


# MCP Tool definitions for Claude Code integration
MCP_TOOLS = [
    {
        "name": "perplexity_search",
        "description": "Perform Perplexity Pro Search with web crawling, real-time data, and verified sources. Returns professional markdown reports with 15-20 source citations. Supports web, social media, and academic sources.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query (any language, auto-detected)",
                },
                "search_type": {
                    "type": "string",
                    "enum": ["pro", "auto", "fast"],
                    "description": "Search type: 'pro' (deep research, recommended), 'auto' (balanced), 'fast' (quick results). Default: 'pro'",
                    "default": "pro",
                },
                "max_tokens": {
                    "type": "integer",
                    "description": "Maximum tokens in response (100-4000). Default: 1024",
                    "default": 1024,
                    "minimum": 100,
                    "maximum": 4000,
                },
                "sources": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": ["web", "social", "scholar"],
                    },
                    "description": "Sources to search: 'web' (general web), 'social' (Twitter/Reddit/forums), 'scholar' (academic papers). Can combine. Default: ['web']",
                    "default": ["web"],
                },
                "language": {
                    "type": "string",
                    "enum": ["en", "de", "es", "fr", "it"],
                    "description": "Response language: 'en' (English), 'de' (Deutsch), 'es' (Español), 'fr' (Français), 'it' (Italiano). Default: 'en'",
                    "default": "en",
                },
                "save_to_file": {
                    "type": "string",
                    "description": "Optional file path to save markdown report (e.g., 'report.md'). Directories created automatically.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "perplexity_social",
        "description": "Search social media and expert forums (Twitter/X, Reddit, forums) with Perplexity Pro Search. Returns professional markdown report with verified source citations.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query for social media/forums (any language, auto-detected)",
                },
                "max_tokens": {
                    "type": "integer",
                    "description": "Maximum tokens in response (100-4000). Default: 1024",
                    "default": 1024,
                    "minimum": 100,
                    "maximum": 4000,
                },
                "save_to_file": {
                    "type": "string",
                    "description": "Optional file path to save markdown report (e.g., 'social_report.md'). Directories created automatically.",
                },
            },
            "required": ["query"],
        },
    },
]


def process_tool_call(tool_name: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process MCP tool calls.

    Args:
        tool_name: Name of the tool
        tool_input: Input parameters for the tool

    Returns:
        Tool execution result
    """
    if tool_name == "perplexity_search":
        return perplexity_search(
            query=tool_input.get("query"),
            search_type=tool_input.get("search_type", "pro"),
            max_tokens=tool_input.get("max_tokens", 1024),
            save_to_file=tool_input.get("save_to_file"),
            sources=tool_input.get("sources"),
            language=tool_input.get("language", "en"),
        )
    elif tool_name == "perplexity_social":
        return perplexity_social(
            query=tool_input.get("query"),
            max_tokens=tool_input.get("max_tokens", 1024),
            save_to_file=tool_input.get("save_to_file"),
        )
    else:
        return {"success": False, "error": f"Unknown tool: {tool_name}"}


if __name__ == "__main__":
    # Test the functions
    print("Testing Perplexity MCP Server\n")

    # Test pro search
    print("1. Testing Pro Search:")
    result = perplexity_search("What are the latest AI trends in 2025?")
    print(f"   Success: {result['success']}")
    if result["success"]:
        print(f"   Content preview: {result['content'][:200]}...")
        print(f"   Citations: {len(result.get('citations', []))} found\n")
    else:
        print(f"   Error: {result['error']}\n")

    # Test social search
    print("2. Testing Social Search:")
    result = perplexity_social("What are developers discussing about AI safety?")
    print(f"   Success: {result['success']}")
    if result["success"]:
        print(f"   Content preview: {result['content'][:200]}...")
        print(f"   Citations: {len(result.get('citations', []))} found\n")
    else:
        print(f"   Error: {result['error']}\n")

    print("Available MCP Tools:")
    for tool in MCP_TOOLS:
        print(f"  - {tool['name']}: {tool['description']}")
