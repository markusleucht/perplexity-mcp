# System Upgrade & Perplexity MCP Setup - COMPLETE ✅

## System Upgrades Completed

### Python Upgrade
- **Before**: Python 3.8.2 (system default)
- **After**: Python 3.12.12 (Homebrew managed)
- **Installation**: `brew install python@3.12`
- **Location**: `/opt/homebrew/bin/python3.12`

### pip Upgrade
- **Before**: pip 19.2.3 (very old, permission issues)
- **After**: pip 25.3 (latest, working in venv)
- **Method**: Virtual environment to bypass system restrictions

### PATH Configuration
Updated `~/.zshrc` and created `~/.zprofile`:
```bash
export PATH="/opt/homebrew/bin:$HOME/.local/bin:$PATH"
```
This ensures Homebrew's Python 3.12 is prioritized over system Python 3.8

## Perplexity MCP Server Setup

### Virtual Environment
- **Location**: `/Users/markus/perplexity/venv/`
- **Python**: 3.12.12
- **pip**: 25.3

### Installed Packages
```
openai==2.8.1          # Perplexity API client
python-dotenv==1.2.1   # Environment variable management
mcp==1.22.0            # Model Context Protocol
```

All dependencies installed successfully with no conflicts.

## Testing Results ✅

Both MCP tools tested and working:

### 1. Pro Search
```
Success: True
Query: "What are the latest AI trends in 2025?"
Result: Agentic AI, generative/multimodal AI, ethical AI, edge models...
```

### 2. Social Search
```
Success: True
Query: "What are developers discussing about AI safety?"
Result: Technical & governance challenges, risks, best practices...
```

## How to Use

### Activate Virtual Environment
```bash
cd /Users/markus/perplexity
source venv/bin/activate
```

### Run the Server
```bash
python src/perplexity_mcp.py
```

### Use in Python Code
```python
from src.perplexity_mcp import perplexity_search, perplexity_social

# Pro search with real-time web data
result = perplexity_search("Your query here")
print(result['content'])

# Social-focused search
result = perplexity_social("Twitter/X topic")
print(result['content'])
```

### Use with Claude Code
Configure in Claude Code settings:
```json
{
  "mcpServers": {
    "perplexity": {
      "command": "/opt/homebrew/bin/python3.12",
      "args": ["-m", "venv", "activate", "&&", "python", "/Users/markus/perplexity/src/perplexity_mcp.py"]
    }
  }
}
```

## Project Structure
```
/Users/markus/perplexity/
├── venv/                      # Virtual environment (Python 3.12)
├── .env                       # API key (not in git)
├── .env.example               # Template
├── .gitignore                 # Ignore venv, .env, etc
├── pyproject.toml             # Project metadata
├── src/
│   ├── __init__.py
│   └── perplexity_mcp.py     # MCP server (~150 lines)
├── README.md                  # Full documentation
├── QUICKSTART.md              # Quick reference
├── SETUP_COMPLETE.md          # This file
└── docs/plan/plan.md          # Implementation plan
```

## API Billing Reminder

You have $5 in Perplexity API credits.

**Cost estimates:**
- Pro Search: $0.20-$0.50 per query
- Social Search: $0.10-$0.20 per query
- **Expected queries**: 25-50 per month

Monitor usage: https://www.perplexity.ai/settings/api

## Next Steps

1. **Whenever you use the project:**
   ```bash
   cd /Users/markus/perplexity
   source venv/bin/activate
   python src/perplexity_mcp.py
   ```

2. **To add new features**, update `src/perplexity_mcp.py`

3. **To use in other projects**, install the package:
   ```bash
   pip install -e /Users/markus/perplexity
   ```

4. **Integrate with Claude Code** by adding MCP server config

## System Info

```
OS: macOS (Darwin 24.2.0)
Architecture: ARM64 (Apple Silicon)
Shell: zsh
Python: 3.12.12 (Homebrew)
pip: 25.3
Homebrew: 4.6.20
```

## Done! 🎉

Your system is now upgraded and your Perplexity MCP server is ready to use across all your projects.
