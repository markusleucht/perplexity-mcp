# Perplexity MCP Project

**Project:** Perplexity MCP server for Claude Code + pharma-research skill
**Purpose:** Deep research with web crawling via natural language queries

---

## For Claude Code Agent: Tool Discovery

> **CRITICAL:** Before using ANY tool in this project, consult the tool manifests below.

### Available Tools

📋 **MCP Server:** [`docs/tools/mcp-servers.md`](docs/tools/mcp-servers.md)
- `mcp__perplexity__perplexity_search` - Pro Search with web crawling
- `mcp__perplexity__perplexity_social` - Social media & forums search
- **Always check parameters, costs, and examples before calling**

🎯 **Skills:** [`docs/tools/skills.md`](docs/tools/skills.md)
- `pharma-research` - German pharmaceutical market research skill (v2.0.0)
- **Check trigger keywords and cost implications**

📦 **Packages:** [`docs/tools/packages.md`](docs/tools/packages.md)
- Python dependencies and system requirements
- **Check before installing new packages**

### When to Consult Manifests

**Before using a tool:**
1. Read `docs/tools/mcp-servers.md` for parameters, returns, costs
2. Check examples for proper usage
3. Verify tool is documented

**Before activating a skill:**
1. Read `docs/tools/skills.md` for triggers and expected behavior
2. Understand cost implications (~$0.06-0.10 per pharma report)
3. Review expected output format

---

## For Users: Documentation

### 🚀 Getting Started
→ [Quick Setup](QUICKSTART.md) - 2 minutes
→ [Complete Guide](docs/guides/QUICKSTART.md) - 5 minutes

### 📖 Usage
→ [User Guide](docs/guides/USER_GUIDE.md) - Examples, tips, output format
→ [Pharma Research](docs/guides/PHARMA_RESEARCH.md) - German market analysis skill

### 🔧 Technical
→ [Developer Guide](docs/guides/DEVELOPER_GUIDE.md) - API reference, parameters, costs
→ [Troubleshooting](docs/guides/TROUBLESHOOTING.md) - Common issues

### 📚 More
→ [Installation](INSTALL.md) - Detailed setup
→ [Changelog](CHANGELOG.md) - All changes

---

## Project Context

**What This Project Does:**
- MCP server integrating Perplexity AI with Claude Code
- Natural language queries → comprehensive markdown reports with sources
- German pharmaceutical market research via specialized skill

**Key Features:**
- Pro Search: Deep research with web crawling (~$0.01-0.02/query)
- Social Search: Twitter/X, Reddit, forums (~$0.01-0.02/query)
- German language support (auto-detected)
- Pharma-research skill: Structured business analysis (~$0.06-0.10/report)

**Specifications:**
- MCP Protocol: See `docs/specs/mcp_research.md`
- SKILL Spec: See `docs/specs/SKILL_SPEC.md`
- Skill validated via `~/.claude/skills/pharma-research/validate_skill.py`

---

**Architecture:** This project follows progressive disclosure. Agent instructions above, user docs in `docs/guides/`, tool manifests in `docs/tools/`, specs in `docs/specs/`.
