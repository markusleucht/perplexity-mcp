# Perplexity MCP Developer Guide

**Last Updated:** November 23, 2025
**Audience:** Developers integrating or extending Perplexity MCP
**Prerequisites:** Python 3.8+, MCP server concepts

---

## Tool Parameters

If you want to be explicit about parameters:

| Parameter | Values | Default | Example |
|-----------|--------|---------|---------|
| `query` | Any text | Required | "AI trends 2025" |
| `search_type` | pro, auto, fast | pro | "fast" |
| `sources` | web, social, scholar | web | "social" |
| `language` | en, de, es, fr, it | en | "de" |
| `max_tokens` | 100-4000 | 1024 | 2000 |
| `save_to_file` | Path/filename | None | "report.md" |

### Example with Parameters
```
Pro Search: "What are the latest cancer treatments?"
German language, save as "Krebsbehandlung_2025.md"
```

---

## Project Structure

```
/Users/markus/perplexity/
├── .env                    # Your API key (never commit)
├── .mcp.json              # MCP server config (already set up)
├── README.md              # Project overview
├── src/
│   └── perplexity_mcp.py  # The actual tool code
├── docs/
│   ├── guides/
│   │   ├── QUICKSTART.md
│   │   ├── USER_GUIDE.md
│   │   ├── DEVELOPER_GUIDE.md
│   │   ├── PHARMA_RESEARCH.md
│   │   └── TROUBLESHOOTING.md
│   ├── tools/
│   │   ├── mcp-servers.md
│   │   ├── skills.md
│   │   └── packages.md
│   ├── specs/
│   │   ├── SKILL_SPEC.md
│   │   └── mcp_research.md
│   └── reports/           # Generated reports
└── reports/               # All generated reports (auto-created)
    ├── Dermatologen_Deutschland_2025.md
    ├── Psoriasis_Therapien_2025.md
    └── ... (your search results)
```

---

## API Costs

- **Pro Search:** ~$0.01-0.02 per query
- **Social Search:** ~$0.01-0.02 per query
- **Your Budget:** $5 in credits
- **Expected Usage:** 100-250 searches before credits depleted

Monitor at: https://www.perplexity.ai/settings/api

---

## API Reference

The MCP tools are defined in `src/perplexity_mcp.py`:

### perplexity_search

```python
def perplexity_search(
    query: str,
    search_type: str = "pro",
    max_tokens: int = 1024,
    sources: list = None,
    language: str = "en",
    save_to_file: str = None,
) -> Dict[str, Any]
```

**Parameters:**
- `query` (str, required): Search query in any language
- `search_type` (str, optional): "pro" (deep research), "auto" (balanced), "fast" (quick)
- `max_tokens` (int, optional): Response length (100-4000)
- `sources` (list, optional): ["web"], ["social"], ["scholar"]
- `language` (str, optional): "en", "de", "es", "fr", "it" (auto-detected)
- `save_to_file` (str, optional): Path to save markdown report

**Returns:**
```python
{
    "success": True/False,
    "content": "Text answer",
    "markdown": "Formatted report",
    "citations": ["url1", "url2", ...],
    "file_saved": "path/to/file.md",  # if requested
    "error": "Error message"  # if failed
}
```

### perplexity_social

```python
def perplexity_social(
    query: str,
    max_tokens: int = 1024,
    save_to_file: str = None,
) -> Dict[str, Any]
```

**Parameters:**
- `query` (str, required): Social media search query
- `max_tokens` (int, optional): Response length (100-4000)
- `save_to_file` (str, optional): Path to save markdown report

**Returns:** Same structure as `perplexity_search`

---

## Integration Patterns

### Basic Integration

```python
# Using the MCP tool through Claude Code
result = mcp__perplexity__perplexity_search(
    query="AI trends 2025",
    search_type="auto",
    language="en"
)

if result["success"]:
    print(result["markdown"])
    print(f"Sources: {len(result['citations'])}")
```

### Saving Reports

```python
# Automatically save to file
result = mcp__perplexity__perplexity_search(
    query="German pharma market analysis",
    language="de",
    save_to_file="reports/pharma_analysis.md"
)

print(f"Report saved to: {result['file_saved']}")
```

### Social Media Research

```python
# Search social media and forums
result = mcp__perplexity__perplexity_social(
    query="What are developers saying about Claude Code?",
    max_tokens=2000
)

# Process results
for citation in result["citations"]:
    print(f"Source: {citation}")
```

---

## Configuration

### Environment Variables

Create `.env` in project root:
```bash
PERPLEXITY_API_KEY=pplx-your-api-key-here
```

### MCP Server Configuration

`.mcp.json` structure:
```json
{
  "mcpServers": {
    "perplexity": {
      "command": "python",
      "args": ["-m", "perplexity_mcp"],
      "env": {
        "PERPLEXITY_API_KEY": "${PERPLEXITY_API_KEY}"
      }
    }
  }
}
```

---

## Testing

### Manual Testing

```bash
# Test basic search
python -c "from perplexity_mcp import perplexity_search; print(perplexity_search('test query'))"

# Test social search
python -c "from perplexity_mcp import perplexity_social; print(perplexity_social('test query'))"
```

### Validation Checklist

- [ ] API key loaded from `.env`
- [ ] MCP server responds to requests
- [ ] Search returns citations
- [ ] German language detection works
- [ ] File saving creates reports in correct location
- [ ] Error handling works for invalid queries

---

## Related Documentation

- **User Guide** → [`USER_GUIDE.md`](USER_GUIDE.md)
- **Troubleshooting** → [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
- **MCP Server Tools** → [`../tools/mcp-servers.md`](../tools/mcp-servers.md) (detailed tool reference)
- **Quick Start** → [`QUICKSTART.md`](QUICKSTART.md)
- **Installation** → [`../../INSTALL.md`](../../INSTALL.md)
- **Perplexity API Docs** → https://docs.perplexity.ai/
