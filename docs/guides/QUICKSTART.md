# Quick Start: Perplexity MCP Server

**Last Updated:** November 23, 2025
**Time to First Search:** 5 minutes
**Audience:** New users getting started

---

## What This Tool Does

With this MCP server, you can ask Claude Code to:
- Search Perplexity AI Pro Search (deep research with web crawling)
- Search social media and expert forums
- Get German-language reports
- Save results as markdown files
- **NEW:** Built-in research guidelines for precise, data-driven answers
- **NEW:** Automated German pharmaceutical market research via `pharma-research` skill

Everything happens through natural language - just ask!

### Research Quality Guidelines

Every search is automatically guided by these principles:
- **Specific data with years** (no generic statements)
- **Context**: changes over time + benchmarks
- **Transparent**: clearly states when data is unavailable
- **Structured**: Key facts → Data points → Interpretation → Sources

---

## Setup

### 1. First-Time Setup (One Command)

If this is your first time using the tool, run:

```bash
chmod +x setup.sh && ./setup.sh
```

This automatically installs dependencies and configures everything. Then restart Claude Code.

**Already set up?** Skip to step 2.

### 2. Verify API Key

Your `.env` file should already have your Perplexity API key:

```bash
cat .env
```

You should see:
```
PERPLEXITY_API_KEY=pplx-...
```

### 3. Test the Server (Optional)

With the venv activated:

```bash
source venv/bin/activate
python src/perplexity_mcp.py
```

Expected output:
```
Testing Perplexity MCP Server

1. Testing Pro Search:
   Success: True
   Content preview: The latest AI trends in 2025...
   Citations: X found

2. Testing Social Search:
   Success: True
   Content preview: Developers are discussing...
   Citations: X found

Available MCP Tools:
  - perplexity_search: Perform a Pro Search on Perplexity AI...
  - perplexity_social: Search social media sources...
```

---

## Using with Claude Code

### Basic Searches

```
Search for "quantum computing trends in 2025"
```

Claude Code will call the tool and return a markdown report with sources.

### Natural Language Examples

#### Pro Search (Deep Research)
```
Search for the latest AI developments in 2025
```
→ Performs deep research with web crawling, returns comprehensive report with 15-20 sources

#### Social Media Focus
```
Search social media for what people are discussing about AI safety
```
→ Searches Twitter, Reddit, forums, expert discussions

#### German Language
```
Search für Entwicklungen in der Medizin 2025
```
→ Returns German-language report (query language detected)

#### Save to File
```
Search for machine learning trends and save to trends.md
```
→ Creates `reports/trends.md` with complete report (automatically saved to `reports/` folder)

#### Language Selection
```
Search for renewable energy trends in Spanish
```
→ Returns Spanish-language response

---

## Claude Code Integration

The MCP server is already configured! Claude Code automatically loads it from:
- **Config file**: `.mcp.json` (server definition)
- **Settings**: `.claude/settings.json` (enabled servers)

In Claude Code, you'll have access to:
- `mcp__perplexity__perplexity_search` - Pro Search with web crawling and real-time data
- `mcp__perplexity__perplexity_social` - Social-focused search (X/Twitter, Reddit)

Claude Code will automatically activate the venv and run the server.

---

## Using Programmatically

With venv activated:

```python
from src.perplexity_mcp import perplexity_search, perplexity_social

# Pro Search (deep research with web crawling)
result = perplexity_search("What are the latest AI trends?")
if result['success']:
    print(result['content'])
else:
    print(f"Error: {result['error']}")

# Social Search (X/Twitter, Reddit focused)
result = perplexity_social("What's trending about AI safety?")
if result['success']:
    print(result['content'])
```

---

## Cost Tracking

Your $5 API credits:
- **Pro Search**: ~$0.01-0.02 per query
- **Social Search**: ~$0.01-0.02 per query
- **Expected Usage**: 100-250 searches before credits depleted

Monitor at: https://www.perplexity.ai/settings/api

---

## Next Steps

1. **Try a simple search** in Claude Code
2. **Review the generated report** in the IDE
3. **Check the sources** - they're all real and verifiable
4. **Customize for your needs** - change language, source type, etc.

### Explore More

- **Detailed Examples** → [`USER_GUIDE.md`](USER_GUIDE.md)
- **Technical Reference** → [`DEVELOPER_GUIDE.md`](DEVELOPER_GUIDE.md)
- **Pharma Research** → [`PHARMA_RESEARCH.md`](PHARMA_RESEARCH.md)
- **Having Issues?** → [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

---

## Troubleshooting Quick Fixes

### "PERPLEXITY_API_KEY not set"
- Verify `.env` exists in project root
- Check API key is valid at https://www.perplexity.ai/settings/api

### "Rate limit exceeded"
- Check usage dashboard
- Wait before next request
- Consider upgrading Perplexity subscription

### "No results returned"
- Try different search query
- Use `search_type="auto"` instead of `"pro"`
- Verify API key has active credits

**For comprehensive troubleshooting** → See [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

---

## Related Documentation

- **User Guide** → [`USER_GUIDE.md`](USER_GUIDE.md) - Examples, tips, output format
- **Developer Guide** → [`DEVELOPER_GUIDE.md`](DEVELOPER_GUIDE.md) - API reference, parameters
- **Troubleshooting** → [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) - Common issues
- **Pharma Research** → [`PHARMA_RESEARCH.md`](PHARMA_RESEARCH.md) - Specialized skill
- **Installation** → [`../../INSTALL.md`](../../INSTALL.md) - Detailed setup
- **Project Overview** → [`../../README.md`](../../README.md) - About this project
