# MCP Servers - Available Tools

**Purpose:** Progressive disclosure of MCP server capabilities installed in this environment.

**Last Updated:** November 23, 2025

---

## Perplexity MCP Server

**Repository:** https://github.com/markusleucht/perplexity-mcp
**Status:** ✅ Active
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

#### 1. `mcp__perplexity__perplexity_search`

**Purpose:** Comprehensive search with web crawling and deep research

**Parameters:**
```python
{
  "query": str,              # Required - Search query (any language)
  "search_type": str,        # Optional - "pro"|"auto"|"fast" (default: "auto")
  "sources": list[str],      # Optional - ["web"]|["social"]|["scholar"] (default: ["web"])
  "language": str,           # Optional - "en"|"de"|"es"|"fr"|"it" (default: "de")
  "max_tokens": int,         # Optional - 100-4000 (default: 1024)
  "save_to_file": str        # Optional - Path to save markdown report
}
```

**Returns:**
```python
{
  "success": bool,
  "content": str,            # Text answer
  "markdown": str,           # Formatted report with citations
  "citations": list[str],    # Source URLs
  "file_saved": str,         # Path if saved
  "error": str               # Error message if failed
}
```

**Cost:** ~$0.005-0.01 per search (auto mode), ~$0.01-0.02 (pro mode)

**Examples:**
```
"Search for German pharmaceutical regulations 2025"
"Find the latest AI developments in healthcare"
"Research Diabetes Type 2 treatment landscape in Germany"
```

#### 2. `mcp__perplexity__perplexity_social`

**Purpose:** Search social media and expert forums (Twitter/X, Reddit, forums)

**Parameters:**
```python
{
  "query": str,              # Required - Social media search query
  "max_tokens": int,         # Optional - 100-4000 (default: 1024)
  "save_to_file": str        # Optional - Path to save report
}
```

**Returns:** Same structure as `perplexity_search`

**Cost:** ~$0.01-0.02 per search

**Examples:**
```
"What are people discussing about AI safety on social media?"
"Find Reddit discussions about Claude Code"
"Search Twitter for opinions on new pharma regulations"
```

### Limitations
- Requires valid Perplexity API key ($5 initial credit)
- Rate limits: Check https://www.perplexity.ai/settings/api
- Language support: EN, DE, ES, FR, IT (auto-detected)
- Max tokens: 4000 per response

### Dependencies
- Python 3.8+
- `perplexity-python` package
- Valid API key in `.env`
- MCP server configuration in `.mcp.json`

### Validation
- Test with: "Search for 'test' using Perplexity"
- Should return search results with sources
- Check API credits at Perplexity dashboard

### Documentation
- Setup: `docs/QUICKSTART.md`
- Examples: `docs/OUTPUT_EXAMPLES.md`
- API docs: https://docs.perplexity.ai/

---

## IDE MCP Server (Built-in)

**Status:** ✅ Active (Built into Claude Code)
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
   ```bash
   # Follow server-specific installation instructions
   ```

2. **Configure in `.mcp.json`**
   ```json
   {
     "mcpServers": {
       "server-name": {
         "command": "...",
         "args": [...],
         "env": {...}
       }
     }
   }
   ```

3. **Document in this file**
   - Add new section with server name
   - List all available tools
   - Document parameters and returns
   - Add examples and limitations
   - Note dependencies and validation steps

4. **Fetch and mirror spec (if available)**
   - Check for official MCP protocol spec
   - Mirror to `docs/MCP_PROTOCOL_SPEC.md` or similar
   - Document version and source URL

5. **Commit and version control**
   ```bash
   git add docs/tools/mcp-servers.md
   git commit -m "docs: add [server-name] MCP server documentation"
   ```

---

## Best Practices

1. **Test before documenting** - Verify all tools work before adding to this manifest
2. **Include costs** - Document any API costs or rate limits
3. **Provide examples** - Show real-world usage for each tool
4. **Update regularly** - When tools change, update documentation immediately
5. **Cross-reference** - Link to detailed docs in main project documentation

---

**This manifest follows the progressive disclosure principle established in CLAUDE.md**
