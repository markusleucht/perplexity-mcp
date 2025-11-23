# Claude Code MCP Integration

Your Perplexity MCP server is now configured and ready to use with Claude Code!

## Configuration

### 1. MCP Server Definition (`.mcp.json`)
```json
{
  "mcpServers": {
    "perplexity": {
      "command": "/opt/homebrew/bin/python3.12",
      "args": ["/Users/markus/perplexity/src/perplexity_mcp.py"],
      "env": {
        "PYTHONPATH": "/Users/markus/perplexity",
        "PYTHONDONTWRITEBYTECODE": "1"
      }
    }
  }
}
```

This tells Claude Code:
- **Server name**: `perplexity`
- **Executable**: Python 3.12.12 (from Homebrew)
- **Script**: The MCP server implementation
- **Environment**: Set Python paths for correct module discovery

### 2. Enable the Server (`.claude/settings.json`)
```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["perplexity"]
}
```

This tells Claude Code:
- Enable all MCP servers in this project
- Specifically approve the `perplexity` server

## Available Tools in Claude Code

Once enabled, Claude Code has access to:

### `perplexity_search`
Perform deep research with real-time web crawling.

**Parameters:**
- `query` (string, required): Search query
- `search_type` (string, optional): "pro" (deep), "auto" (automatic), "fast" (quick)
- `max_tokens` (integer, optional): Response length (100-4000)

**Example in Claude Code:**
```
perplexity_search("What are the latest breakthroughs in quantum computing?", search_type="pro")
```

### `perplexity_social`
Search social media platforms (X/Twitter, Reddit, etc).

**Parameters:**
- `query` (string, required): Social media query
- `max_tokens` (integer, optional): Response length (100-4000)

**Example in Claude Code:**
```
perplexity_social("What are developers discussing about Web3 security?")
```

## How It Works

1. Claude Code reads `.mcp.json` to discover available MCP servers
2. Claude Code reads `.claude/settings.json` to see which servers are enabled
3. When you ask Claude Code to use a tool, it:
   - Launches the Python interpreter
   - Runs `/Users/markus/perplexity/src/perplexity_mcp.py`
   - Calls the requested tool with your parameters
   - Returns results back to Claude Code

## Using It in Claude Code

Just ask naturally:

```
Use perplexity_search to find the latest information about AI safety regulations in 2025.
```

Or in multimodal contexts:

```
Can you search for recent news about this topic using perplexity_search and then summarize it?
```

Claude Code will automatically:
- Activate the virtual environment
- Load your `.env` API key
- Execute the search
- Parse and return the results

## Virtual Environment Handling

The virtual environment at `/Users/markus/perplexity/venv/` is automatically detected and activated by Claude Code because:
- It's in the project directory
- The MCP server command uses the full path to Python 3.12

No manual activation needed when using through Claude Code!

## Troubleshooting

### Server Not Found
If Claude Code says "server not found":
1. Verify `.mcp.json` exists in project root
2. Check `.claude/settings.json` has `"enabledMcpjsonServers": ["perplexity"]`
3. Reload Claude Code settings (usually automatic)

### API Key Error
If you see "PERPLEXITY_API_KEY not set":
1. Verify `.env` file in project root has valid API key
2. Check API key is still valid at https://www.perplexity.ai/settings/api

### No Results Returned
If search returns empty:
1. Try rephrasing the query
2. Use different `search_type` ("auto" often works better than "pro")
3. Check API credits at https://www.perplexity.ai/settings/api

## File Locations

```
/Users/markus/perplexity/
├── .mcp.json                  # MCP server definition (NEW)
├── .claude/
│   └── settings.json          # MCP settings (NEW)
├── venv/                       # Virtual environment
│   ├── bin/
│   │   └── python            # Python 3.12.12
│   └── lib/
│       └── python3.12/
│           └── site-packages/ # Dependencies
├── src/
│   └── perplexity_mcp.py      # Server implementation
├── .env                        # API key (secret)
└── QUICKSTART.md              # Quick reference
```

## Security Notes

- `.env` is in `.gitignore` - never commit your API key
- `.mcp.json` is safe to commit - it only contains paths and no secrets
- `.claude/settings.json` is safe to commit - enables the server for the team
- API key is only read at runtime from `.env`

## Next Steps

The setup is complete! You can now:

1. **In Claude Code**, ask it to use the Perplexity tools:
   ```
   Search for the latest AI models using perplexity_search
   ```

2. **In other projects**, you can link to this MCP:
   ```bash
   # Copy .mcp.json and .claude/settings.json to another project
   # Point to this shared server
   ```

3. **Monitor costs**:
   - Check usage at https://www.perplexity.ai/settings/api
   - You have $5 in API credits
   - Each search costs $0.10-$0.50 depending on type
