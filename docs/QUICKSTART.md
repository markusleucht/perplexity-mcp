# Quick Start: Perplexity MCP Server

## 1. Activate Virtual Environment

The project uses Python 3.12.12 in an isolated virtual environment:

```bash
cd /Users/markus/perplexity
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt. All dependencies are pre-installed.

## 2. Verify API Key

Your `.env` file should already have your Perplexity API key:

```bash
cat .env
```

You should see:
```
PERPLEXITY_API_KEY=pplx-...
```

## 3. Test the Server

With the venv activated:

```bash
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

## 4. Use in Your Code

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

## 5. Claude Code Integration

The MCP server is already configured! Claude Code automatically loads it from:
- **Config file**: `.mcp.json` (server definition)
- **Settings**: `.claude/settings.json` (enabled servers)

In Claude Code, you'll have access to:
- `perplexity_search` - Pro Search with web crawling and real-time data
- `perplexity_social` - Social-focused search (X/Twitter, Reddit)

Claude Code will automatically activate the venv and run the server.

## Cost Tracking

Your $5 API credits:
- **Pro Search**: ~$0.20-$0.50 per query
- **Social Search**: ~$0.10-$0.20 per query

Monitor at: https://www.perplexity.ai/settings/api

## Troubleshooting

**"PERPLEXITY_API_KEY not set"**
- Verify `.env` exists in project root
- Check API key is valid at https://www.perplexity.ai/settings/api

**"Rate limit exceeded"**
- Check usage dashboard
- Wait before next request
- Consider upgrading Perplexity subscription

**"No results returned"**
- Try different search query
- Use `search_type="auto"` instead of `"pro"`
- Verify API key has active credits
