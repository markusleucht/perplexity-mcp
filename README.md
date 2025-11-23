# Perplexity MCP Server

A lean MCP (Model Context Protocol) server for Perplexity AI with Pro Search and social-focused search capabilities. Integrates seamlessly with Claude Code and other MCP-compatible clients.

## Features

- **Pro Search**: Deep research with streaming support and real-time web crawling
- **Social Search**: Focus queries on X/Twitter, Reddit, and other social platforms
- **Cost-Efficient**: Streaming prevents unnecessary token usage with your $5 API credits
- **Lean**: Minimal dependencies (~100 lines of core code)
- **Context-Aware**: MCP protocol enables natural integration with Claude Code

## Setup

### One-Command Setup (Recommended)

```bash
chmod +x setup.sh && ./setup.sh
```

This will:
- Auto-detect your Python installation
- Install required packages (`openai`, `python-dotenv`)
- Update `.mcp.json` with correct Python path
- Verify the setup

Then restart Claude Code.

### Manual Setup

See [INSTALL.md](INSTALL.md) for detailed manual installation instructions.

### Configure API Key

1. Get your Perplexity API key from [https://www.perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)
2. Create a `.env` file:
   ```bash
   echo "PERPLEXITY_API_KEY=pplx-your-key-here" > .env
   ```

**Important**: Never commit `.env` to version control. It's in `.gitignore` by default.

### Auto-Install Feature

The MCP server now auto-installs missing dependencies on first run. No manual pip install needed!

## Usage

### Python Module

```python
from src.perplexity_mcp import perplexity_search, perplexity_social

# Pro Search
result = perplexity_search("What are the latest AI trends?", search_type="pro")
print(result['content'])
print(f"Citations: {result['citations']}")

# Social-Focused Search
result = perplexity_social("What's trending about AI safety on Twitter?")
print(result['content'])
```

### Command Line Test

```bash
cd /Users/markus/perplexity
python src/perplexity_mcp.py
```

### Claude Code Integration

The MCP server exposes two tools for Claude Code:

#### 1. `perplexity_search`
Perform deep research with web crawling.

**Parameters:**
- `query` (string, required): The search query
- `search_type` (string, default: "pro"): "pro", "auto", or "fast"
- `max_tokens` (integer, default: 1024): Response length (100-4000)

**Response:**
```json
{
  "success": true,
  "content": "Search results...",
  "citations": ["url1", "url2"],
  "search_type": "pro"
}
```

#### 2. `perplexity_social`
Search social media platforms (X, Reddit, etc).

**Parameters:**
- `query` (string, required): The social media query
- `max_tokens` (integer, default: 1024): Response length (100-4000)

**Response:**
```json
{
  "success": true,
  "content": "Social media insights...",
  "citations": ["url1", "url2"],
  "search_focus": "social"
}
```

## Project Structure

```
/Users/markus/perplexity/
├── .env                      # Your API key (never commit)
├── .env.example              # Template for API keys
├── .gitignore                # Git ignore rules
├── README.md                 # This file
├── pyproject.toml            # Python project config
├── src/
│   └── perplexity_mcp.py    # MCP server implementation
└── docs/
    ├── guides/               # User-facing documentation
    │   ├── QUICKSTART.md     # Quick start guide
    │   ├── USER_GUIDE.md     # End user examples & tips
    │   ├── DEVELOPER_GUIDE.md # Technical API reference
    │   ├── PHARMA_RESEARCH.md # Pharma skill guide
    │   └── TROUBLESHOOTING.md # Common issues
    ├── tools/                # Tool manifests
    │   ├── mcp-servers.md    # MCP server capabilities
    │   ├── skills.md         # Installed skills
    │   └── packages.md       # Package inventory
    ├── specs/                # Mirrored specifications
    └── reports/              # Generated research reports
```

## Documentation

### Quick Start
→ [QUICKSTART.md](QUICKSTART.md) - 2 minute setup
→ [docs/guides/QUICKSTART.md](docs/guides/QUICKSTART.md) - Comprehensive guide

### User Documentation
→ [docs/guides/USER_GUIDE.md](docs/guides/USER_GUIDE.md) - Examples, tips, output format
→ [docs/guides/PHARMA_RESEARCH.md](docs/guides/PHARMA_RESEARCH.md) - German pharma market research

### Developer Documentation
→ [docs/guides/DEVELOPER_GUIDE.md](docs/guides/DEVELOPER_GUIDE.md) - API reference, parameters
→ [INSTALL.md](INSTALL.md) - Detailed installation instructions

### Support
→ [docs/guides/TROUBLESHOOTING.md](docs/guides/TROUBLESHOOTING.md) - Common issues & solutions
→ [CLAUDE.md](CLAUDE.md) - System guidelines & progressive disclosure

## API Costs

With your $5 API credits:
- **Pro Search**: ~$0.20-$0.50 per query (deeper analysis)
- **Social Search**: ~$0.10-$0.20 per query (focused results)
- Estimated: 25-50 queries per month with Pro tier

Monitor usage in your [Perplexity dashboard](https://www.perplexity.ai/settings/api).

## Limitations

- Perplexity Pro tier is required for API access
- Rate limits apply per plan (check dashboard)
- Streaming is enabled for Pro Search to optimize token usage
- Social searches limited to sources parameter; cannot scrape directly

## Future Enhancements

- Streaming response handling for real-time updates
- Response caching to reduce API calls
- Batch query support
- Custom system prompts
- Integration with additional APIs (Tavily, etc)

## Troubleshooting

**Error: "PERPLEXITY_API_KEY not set"**
- Ensure `.env` exists in the project root
- Check the API key is valid at [https://www.perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)

**Error: "Rate limit exceeded"**
- Check your usage at [https://www.perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)
- Wait before making more requests
- Consider upgrading your Perplexity subscription

**No results returned**
- Verify your search query is valid
- Try a different `search_type` ("pro" vs "auto")
- Check your API key has active credits

## License

MIT
