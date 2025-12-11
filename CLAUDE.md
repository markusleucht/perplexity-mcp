# Perplexity MCP Project

**Project:** Perplexity MCP server for Claude Code + pharma-research skill
**Purpose:** Deep research with web crawling via natural language queries

---

## Tool Discovery

> **CRITICAL:** Before using ANY tool in this project, consult the tool manifests below.

### Available Tools

📋 **MCP Server:** [`docs/tools/mcp-servers.md`](docs/tools/mcp-servers.md)
- `mcp__perplexity__perplexity_pro` - Pro Search (sonar-pro, 200K context) - quick research, social, academic
- `mcp__perplexity__perplexity_deep` - Deep Research (sonar-deep-research) - exhaustive analysis
- **Check manifest for parameters and examples before calling**

🎯 **Skills:** [`docs/tools/skills.md`](docs/tools/skills.md)
- `pharma-research` - German pharmaceutical market research skill (v2.0.0)
- **Check trigger keywords and cost implications**

📦 **Packages:** [`docs/tools/packages.md`](docs/tools/packages.md)
- Python dependencies and system requirements
- **Check before installing new packages**

### When to Consult Manifests

**Before using a tool:**
1. Read `docs/tools/mcp-servers.md` for parameters and returns
2. Check examples for proper usage
3. Verify tool is documented

**Before activating a skill:**
1. Read `docs/tools/skills.md` for triggers and expected behavior
2. Understand cost implications (~$0.06-0.10 per pharma report)
3. Review expected output format

---

## Project Context

**What This Project Does:**
- MCP server integrating Perplexity AI with Claude Code
- Natural language queries → comprehensive markdown reports with sources
- German pharmaceutical market research via specialized skill

**Key Features:**
- Pro Search: Quick research with configurable sources (web, social, scholar)
- Deep Research: Exhaustive analysis with maximum reasoning
- German response language by default (searches global sources)
- Auto-enrichment for pharma queries (5-year timeframe, entity expansion)
- Report output: `docs/reports/{ddMMYY}_{name}/` with raw Perplexity data

**Specifications:**
- MCP Protocol: See `docs/specs/mcp_research.md`
- SKILL Spec: See `docs/specs/SKILL_SPEC.md`
- Skill validated via `~/.claude/skills/pharma-research/validate_skill.py`

---

**Documentation for users:** See `README.md` for user-facing documentation and quick start guides.
