# MCP Servers - Available Tools

**Purpose:** Progressive disclosure of MCP server capabilities installed in this environment.

**Last Updated:** December 11, 2025

---

## Perplexity MCP Server

**Repository:** https://github.com/markusleucht/perplexity-mcp
**Status:** Active
**Configuration:** `.mcp.json`
**API Key:** `.env` (PERPLEXITY_API_KEY)

### What It Does
Deep research with web crawling, social media search, and real-time data from Perplexity AI.

### When to Use
- Research tasks requiring current information
- German pharmaceutical market analysis
- Social media sentiment analysis
- Academic research with citations
- Competitive intelligence gathering
- Market research with verified sources

### Available Tools

#### 1. `mcp__perplexity__perplexity_pro`

**Purpose:** Pro Search with sonar-pro model (200K context)

**Features:**
- `search_context_size: high` (maximum search depth)
- Configurable sources: web, social, scholar
- Configurable recency filter
- German output by default (searches global sources)

**Parameters:**
```python
{
  "query": str,                    # Required - Search query (any language)
  "sources": list[str],            # Optional - ["web"]|["social"]|["scholar"] (default: ["web"])
  "search_recency_filter": str,    # Optional - "day"|"week"|"month"|"year" (default: None)
  "response_language": str,        # Optional - "de"|"en"|"es"|"fr"|"it" (default: "de")
  "report_name": str               # Optional - Save to docs/reports/{date}_{name}/
}
```

**Returns:**
```python
{
  "success": bool,
  "content": str,              # Raw Perplexity response (markdown)
  "citations": list[str],      # URL array
  "search_results": [          # Rich source data
    {"title": str, "url": str, "date": str}
  ],
  "metadata": {
    "model": "sonar-pro",
    "sources": list,
    "response_language": str,
    "search_context_size": "high",
    "timestamp": str
  },
  "report_saved": str          # Folder path if saved
}
```

**Report Output (if report_name provided):**
```
docs/reports/{ddMMYY}_{report_name}/
├── content.md          # Raw response text
├── citations.json      # URL array
└── search_results.json # Rich source data
```

**Use for:**
- Quick research tasks
- Current events and news
- Social media sentiment (`sources=["social"]`)
- Academic papers (`sources=["scholar"]`)
- Competitive intelligence snapshots

**Examples:**
```
perplexity_pro(query="German pharmaceutical regulations 2025")
perplexity_pro(query="AI healthcare trends", sources=["scholar"])
perplexity_pro(query="Ozempic discussions", sources=["social"], report_name="ozempic_social")
```

---

#### 2. `mcp__perplexity__perplexity_deep`

**Purpose:** Deep Research with sonar-deep-research model

**Maximum quality settings:**
- `reasoning_effort: high`
- `search_context_size: high`
- NO token limits (full output)
- Raw, unaltered Perplexity response

**Features:**
- Auto-detects pharma queries and applies enrichment
- Default pharma marketing agency context (Berlin)
- 5-year default timeframe via prompt enrichment
- Comprehensive source citations

**Parameters:**
```python
{
  "query": str,                # Required - Research query (any topic)
  "context_hint": str,         # Optional - "pharma"|"market"|"tech" (auto-detected)
  "skip_enrichment": bool,     # Optional - Send raw query without optimization (default: False)
  "report_name": str           # Optional - Save to docs/reports/{date}_{name}/
}
```

**Returns:**
```python
{
  "success": bool,
  "content": str,              # FULL Perplexity response (no summarization)
  "citations": list[str],      # URL array
  "search_results": [          # Rich source data
    {"title": str, "url": str, "date": str}
  ],
  "metadata": {
    "model": "sonar-deep-research",
    "reasoning_effort": "high",
    "search_context_size": "high",
    "enriched_query": str,     # What was actually sent
    "enrichment_applied": bool,
    "entities_detected": {},   # Detected drugs, indications, etc.
    "context_applied": [],
    "timestamp": str
  },
  "report_saved": str          # Folder path if saved
}
```

**Report Output (if report_name provided):**
```
docs/reports/{ddMMYY}_{report_name}/
├── content.md          # Raw response text
├── citations.json      # URL array
└── search_results.json # Rich source data
```

**Prompt Enrichment:**
Queries are automatically enriched following Perplexity best practices:
- Drug/indication entity expansion (e.g., "Bimzelx" → "Bimzelx (Bimekizumab) UCB IL-17A/F Inhibitor")
- Temporal context (last 5 years)
- Geographic context (Germany)
- Pharma market keywords (if pharma query detected)

**Use for:**
- Comprehensive market research
- Detailed product analysis
- In-depth competitive intelligence
- Any topic requiring exhaustive research

**Examples:**
```
perplexity_deep(query="Analysiere Bimzelx fuer Psoriasis von UCB - Marktposition Deutschland")
perplexity_deep(query="Wie entwickelt sich der deutsche E-Auto-Markt?", context_hint="market")
perplexity_deep(query="KI-Regulierung der EU", report_name="eu_ai_regulation")
```

---

### Limitations
- Requires valid Perplexity API key
- Rate limits: Check https://www.perplexity.ai/settings/api
- Language support: DE, EN, ES, FR, IT (response language, NOT search filter)
- Deep research model has lower rate limits than pro

### Dependencies
- Python 3.8+
- `openai` package (Perplexity uses OpenAI-compatible API)
- `mcp` package (FastMCP)
- Valid API key in `.env`
- MCP server configuration in `.mcp.json`

### Validation
- Test with: `perplexity_pro(query="test")`
- Should return search results with sources
- Check API credits at Perplexity dashboard

### Documentation
- Setup: `docs/QUICKSTART.md`
- API Reference: `docs/guides/PERPLEXITY_API_REFERENCE.md`
- Official docs: https://docs.perplexity.ai/

---

## IDE MCP Server (Built-in)

**Status:** Active (Built into Claude Code)
**No configuration required**

### Available Tools

#### 1. `mcp__ide__getDiagnostics`
**Purpose:** Get language diagnostics from VS Code
**When to use:** Check for errors, warnings, type issues in code

#### 2. `mcp__ide__executeCode`
**Purpose:** Execute Python code in Jupyter kernel
**When to use:** Run Python code in notebooks, test code snippets

---

## Adding New MCP Servers

When installing a new MCP server:

1. **Install the server**
2. **Configure in `.mcp.json`**
3. **Document in this file**
4. **Test all tools**
5. **Commit changes**

---

**This manifest follows the progressive disclosure principle established in CLAUDE.md**
