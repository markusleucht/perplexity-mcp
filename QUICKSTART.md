# Perplexity MCP Quick Start

Get up and running in 2 minutes.

## Step 1: Setup (30 seconds)

```bash
cd /Users/markus/perplexity
chmod +x setup.sh
./setup.sh
```

The script will automatically:
- Find your Python installation
- Install dependencies
- Configure the MCP server

## Step 2: Add API Key (30 seconds)

```bash
echo "PERPLEXITY_API_KEY=pplx-your-key-here" > .env
```

Get your key from: https://www.perplexity.ai/settings/api

## Step 3: Restart Claude Code (10 seconds)

Close and reopen Claude Code to load the MCP server.

## Step 4: Test It (30 seconds)

Ask Claude Code:

```
Search for "latest developments in quantum computing"
```

You should get a comprehensive markdown report with 15-20 sources.

## That's It!

You're ready to use Perplexity searches in Claude Code.

---

## Common First-Time Issues

### "Python not found"

Install Python 3.8+:
- **macOS**: `brew install python3`
- **Ubuntu/Debian**: `sudo apt install python3 python3-pip`

### "API key not found"

Make sure `.env` exists in `/Users/markus/perplexity/` with:
```
PERPLEXITY_API_KEY=pplx-...
```

### "MCP server not responding"

1. Check `.mcp.json` has correct Python path: `which python3`
2. Restart Claude Code completely
3. Check MCP logs in Claude Code settings

---

## What Can You Do?

### Pro Search (Default)
```
Search for "AI safety research papers 2025"
```

### German Language
```
Suche nach "Entwicklungen in der KI 2025"
```

### Social Media Focus
```
Search social media for discussions about AI regulation
```

### Save to File
```
Search for "Python async programming best practices" and save to python_guide.md
```

### Academic Sources
```
Search for quantum computing papers in scholar sources
```

---

## Next Steps

- **Complete Guide**: See [docs/guides/QUICKSTART.md](docs/guides/QUICKSTART.md)
- **Usage Examples**: See [docs/guides/USER_GUIDE.md](docs/guides/USER_GUIDE.md)
- **Technical Reference**: See [docs/guides/DEVELOPER_GUIDE.md](docs/guides/DEVELOPER_GUIDE.md)
- **Troubleshooting**: See [docs/guides/TROUBLESHOOTING.md](docs/guides/TROUBLESHOOTING.md) or [INSTALL.md](INSTALL.md)
- **Project Overview**: See [README.md](README.md)

---

**Questions?** Check the docs or test the setup:

```bash
python3 src/perplexity_mcp.py
```
