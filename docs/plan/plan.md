# Perplexity MCP Server Setup Plan

## Goal
Create a lean MCP (Model Context Protocol) server for Perplexity AI that enables:
- Pro Search with streaming support
- Social-focused searches (X/Twitter, Reddit)
- Direct integration with Claude Code
- Reusable across projects

## Implementation Steps

### 1. Project Structure
```
/Users/markus/perplexity/
├── .env                    # API key storage
├── .env.example           # Template for API keys
├── src/
│   └── perplexity_mcp.py # MCP server implementation
├── pyproject.toml         # Python dependencies
└── README.md              # Usage instructions
```

### 2. Create `.env` and `.env.example`
- Add `PERPLEXITY_API_KEY=your_key_here` to `.env`
- Create `.env.example` template for documentation
- Add `.env` to `.gitignore` (if using git)

### 3. Build MCP Server (`src/perplexity_mcp.py`)
**Tools to expose:**
- `perplexity_search`: Pro search with streaming
  - Parameters: `query` (string), `search_type` (pro/auto), `max_tokens` (optional)
- `perplexity_social`: Social-focused search
  - Parameters: `query` (string), `sources` (["social"] preset)

**Key features:**
- Use `python-dotenv` for env var loading
- OpenAI SDK with Perplexity base URL
- Streaming responses for Pro Search
- Error handling for rate limits/API errors

### 4. Dependencies (`pyproject.toml`)
- `openai` (Perplexity-compatible SDK)
- `python-dotenv` (environment variable management)
- `mcp` (Model Context Protocol SDK)

### 5. Claude Code Integration
Create MCP server config for Claude Code to auto-discover the server

## Why This Approach?
- **Lean**: Minimal dependencies, ~100 lines of code
- **Context-aware**: MCP protocol lets Claude Code use it naturally
- **Reusable**: Can be called from any MCP-compatible client
- **Cost-effective**: Streaming prevents unnecessary token usage

## Next Steps
1. Create `.env` files
2. Write `src/perplexity_mcp.py` with two tools
3. Add `pyproject.toml` with dependencies
4. Create simple README with usage examples
5. Test with Claude Code
