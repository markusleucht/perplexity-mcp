# Perplexity MCP Installation

## Automatic Setup (Recommended)

Run the setup script to automatically install dependencies and configure the environment:

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Detect your Python installation
- Install required packages (openai, python-dotenv)
- Update .mcp.json with correct Python path
- Verify your setup

## Manual Setup

If the automatic setup doesn't work, follow these steps:

### 1. Check Python Installation

```bash
which python3
python3 --version
```

You need Python 3.8 or higher.

### 2. Install Dependencies

```bash
python3 -m pip install --user -r requirements.txt
```

Or install directly:

```bash
python3 -m pip install --user openai python-dotenv
```

### 3. Configure API Key

Create a `.env` file in the project root:

```bash
echo "PERPLEXITY_API_KEY=pplx-your-key-here" > .env
```

Get your API key from: https://www.perplexity.ai/settings/api

### 4. Update .mcp.json

Find your Python path:

```bash
which python3
```

Edit `.mcp.json` and replace the `command` value with your Python path:

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "/usr/bin/python3",  <-- Your Python path here
      "args": ["/Users/markus/perplexity/src/perplexity_mcp.py"],
      "env": {
        "PYTHONPATH": "/Users/markus/perplexity",
        "PYTHONDONTWRITEBYTECODE": "1"
      }
    }
  }
}
```

### 5. Test the Setup

```bash
python3 src/perplexity_mcp.py
```

You should see test output showing successful searches.

### 6. Restart Claude Code

Close and reopen Claude Code to load the MCP server.

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"

The dependencies aren't installed. Run:

```bash
python3 -m pip install --user openai python-dotenv
```

### "PERPLEXITY_API_KEY not set"

Create a `.env` file with your API key:

```bash
echo "PERPLEXITY_API_KEY=pplx-your-key" > .env
```

### "command not found: /opt/homebrew/bin/python3.12"

Your `.mcp.json` has the wrong Python path. Update it with:

```bash
which python3
```

Then edit `.mcp.json` with the correct path.

### Dependencies auto-install on first run

The MCP server now automatically installs missing dependencies on first run. If you see:

```
📦 Installing missing dependencies: openai>=1.0.0, python-dotenv>=0.19.0
✓ Dependencies installed successfully
```

This is normal and means the setup is working correctly.

## Usage

Once installed, simply ask Claude Code to search:

```
Search for "AI trends in 2025"
```

The tool will automatically:
- Perform a Perplexity Pro Search
- Return a markdown report with sources
- Save to file if requested

See [`docs/guides/USER_GUIDE.md`](docs/guides/USER_GUIDE.md) for detailed usage examples and [`docs/guides/TROUBLESHOOTING.md`](docs/guides/TROUBLESHOOTING.md) for common issues.
