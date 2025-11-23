# Python Packages & System Tools

**Purpose:** Progressive disclosure of installed packages and their purpose.

**Last Updated:** November 23, 2025

---

## Python Packages

### perplexity-python

**Purpose:** Python client for Perplexity AI API
**Version:** Latest (pip installed)
**Used by:** Perplexity MCP Server
**Location:** Python site-packages

**What it does:**
- Provides Python interface to Perplexity AI search API
- Handles authentication and request formatting
- Manages API responses and error handling

**When it's used:**
- Every `mcp__perplexity__perplexity_search` call
- Every `mcp__perplexity__perplexity_social` call
- Background: MCP server initialization

**Dependencies:**
- `requests` (HTTP client)
- `python-dotenv` (environment variable management)

**Documentation:** https://docs.perplexity.ai/

---

### python-dotenv

**Purpose:** Load environment variables from `.env` files
**Version:** Latest (pip installed)
**Used by:** Perplexity MCP Server, various scripts

**What it does:**
- Reads `.env` files and loads variables into environment
- Keeps secrets out of code and version control
- Provides consistent environment configuration

**When it's used:**
- MCP server startup (loads PERPLEXITY_API_KEY)
- Any script using `load_dotenv()`

**Example `.env`:**
```bash
PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxx
```

---

### mcp (Model Context Protocol)

**Purpose:** Protocol for connecting Claude Code with external tools
**Version:** Built into Claude Code
**Used by:** All MCP servers

**What it does:**
- Defines standard protocol for tool communication
- Enables Claude Code to discover and use external tools
- Handles JSON-RPC communication between Claude and MCP servers

**When it's used:**
- Automatically when Claude Code starts
- Every time an `mcp__*` tool is called

**Documentation:**
- Claude Code docs: https://code.claude.com/docs
- MCP protocol spec: (Mirror to `docs/MCP_PROTOCOL_SPEC.md` when available)

---

## System Tools

### git

**Purpose:** Version control system
**Status:** ✅ Installed
**Used by:** All development workflows

**What it does:**
- Tracks file changes and history
- Enables collaboration via GitHub
- Supports branching and merging

**When it's used:**
- Committing changes
- Pushing to GitHub
- Cloning repositories
- Version management

---

### gh (GitHub CLI)

**Purpose:** GitHub command-line interface
**Status:** ✅ Installed (v2.83.0)
**Authenticated:** ✅ Yes (user: markusleucht)

**What it does:**
- Create repositories
- Manage issues and pull requests
- View GitHub data from terminal

**When it's used:**
- Creating repos: `gh repo create`
- Managing PRs: `gh pr create`
- Viewing repos: `gh repo list`

**Documentation:** https://cli.github.com/

---

### python3

**Purpose:** Python interpreter
**Version:** 3.x (system installed)
**Location:** `/usr/bin/python3`, `/opt/homebrew/bin/python3`

**What it does:**
- Executes Python code
- Runs MCP servers
- Executes validation scripts

**When it's used:**
- Running MCP servers: `python3 src/perplexity_mcp_server.py`
- Running scripts: `python3 validate_skill.py`
- Package management: `pip3 install`

---

## Adding New Packages

When installing a new package or tool:

1. **Install the package**
   ```bash
   pip3 install package-name
   # or
   brew install tool-name
   ```

2. **Document in this file**
   - Add new section with package name
   - Explain what it does (core functionality)
   - Document when it's used (use cases)
   - Note dependencies
   - Link to documentation

3. **Update requirements (if Python package)**
   ```bash
   # Add to requirements.txt
   echo "package-name==x.y.z" >> requirements.txt
   ```

4. **Commit documentation**
   ```bash
   git add docs/tools/packages.md requirements.txt
   git commit -m "docs: add [package-name] package documentation"
   ```

---

## Best Practices

1. **Pin versions** - Use specific versions in `requirements.txt` for reproducibility
2. **Document purpose** - Explain why the package is needed, not just what it is
3. **Note dependencies** - List what depends on this package
4. **Keep updated** - Update this manifest when packages are added/removed/upgraded
5. **Security** - Never commit API keys or secrets; use `.env` files

---

## Dependency Management

### requirements.txt

**Location:** `/Users/markus/perplexity/requirements.txt`

**Current packages:**
```
perplexity-python
python-dotenv
```

**Regenerate from environment:**
```bash
pip3 freeze > requirements.txt
```

**Install from requirements:**
```bash
pip3 install -r requirements.txt
```

---

## Virtual Environments

**Recommendation:** Use virtual environments for Python projects

**Setup:**
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

**Deactivate:**
```bash
deactivate
```

---

**This manifest follows the progressive disclosure principle established in CLAUDE.md**
