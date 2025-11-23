# System-Level Best Practices for Claude Code

> **READ THIS FIRST:** These guidelines apply to ALL work in this project, before using any external tools, MCP servers, or skills.

## 1. Specification Management

**Principle: Mirror specifications locally before implementation**

When working with external tools, MCP servers, or skills:

1. **Always fetch and mirror official specifications locally**
   - Store in `docs/specs/` directory (e.g., `docs/specs/SKILL_SPEC.md`, `docs/specs/MCP_SPEC.md`)
   - Include version number and date retrieved
   - Document source URL for future updates
   - Enables offline validation and audit trail

2. **Validate against specifications**
   - Create validation scripts when implementing specs (e.g., `validate_skill.py`)
   - Run validation before committing
   - Document any deviations from spec with rationale

3. **Keep specifications version-controlled**
   - Commit spec mirrors to repository
   - Update when official specs change
   - Maintain changelog of spec versions used

**Example: SKILL Specification**
- Mirrored at: `docs/specs/SKILL_SPEC.md`
- Validation: `~/.claude/skills/*/validate_skill.py`
- Official source: https://github.com/anthropics/skills

## 2. Progressive Disclosure of Tool Capabilities

**Principle: Document tool capabilities incrementally as they're discovered**

When new tools (MCP servers, skills, packages) are installed:

1. **Create capability manifests in `docs/tools/`**
   ```
   docs/tools/
   ├── mcp-servers.md          # Available MCP servers & their tools
   ├── skills.md               # Installed skills & their triggers
   └── packages.md             # Python/system packages & their purpose
   ```

2. **Document each tool with:**
   - **What it does** (core functionality)
   - **When to use it** (triggers, use cases)
   - **How to use it** (parameters, examples)
   - **Limitations** (known constraints, costs)
   - **Dependencies** (what it requires)

3. **Update manifests incrementally**
   - Add entries when tools are installed
   - Update when capabilities change
   - Remove when tools are deprecated
   - Version control all changes

4. **Cross-reference from main CLAUDE.md**
   - Keep CLAUDE.md high-level
   - Link to detailed docs in `docs/tools/` and `docs/guides/`
   - Follow progressive disclosure: overview → details → reference

## 3. Best Practice Adherence

**Before implementing ANY tool or skill:**

✅ Check if official specification exists
✅ Mirror specification locally to `docs/specs/`
✅ Create validation mechanism (script, checklist, CI check)
✅ Document tool capabilities in `docs/tools/`
✅ Update main CLAUDE.md with high-level overview
✅ Add examples and troubleshooting to appropriate guide
✅ Version control everything

**Example workflow:**
1. Install MCP server → Fetch MCP protocol spec → Mirror to `docs/specs/MCP_SPEC.md`
2. Configure tools → Document in `docs/tools/mcp-servers.md`
3. Test functionality → Add examples to `docs/guides/`
4. Validate compliance → Run validation script
5. Commit with comprehensive documentation

## 4. Documentation Structure

```
project/
├── CLAUDE.md                    # High-level guide + routing (you are here)
├── docs/
│   ├── guides/                  # User-facing guides
│   │   ├── QUICKSTART.md        # Getting started
│   │   ├── USER_GUIDE.md        # End user reference
│   │   ├── DEVELOPER_GUIDE.md   # Technical reference
│   │   ├── PHARMA_RESEARCH.md   # Specialized use case
│   │   └── TROUBLESHOOTING.md   # Common issues
│   ├── specs/                   # Mirrored specifications
│   │   ├── SKILL_SPEC.md        # SKILL specification
│   │   └── mcp_research.md      # MCP research notes
│   ├── tools/                   # Progressive disclosure docs
│   │   ├── mcp-servers.md       # All MCP servers & their tools
│   │   ├── skills.md            # All skills & their triggers
│   │   └── packages.md          # All packages & their purpose
│   ├── reports/                 # Generated reports & analyses
│   └── archive/                 # Old documentation
├── .claude/
│   └── skills/                  # Skill implementations
│       └── skill-name/
│           ├── SKILL.md         # Core definition (minimal)
│           ├── references/      # Detailed docs
│           └── validate_*.py    # Validation scripts
└── src/                         # Source code
```

## 5. Quality Standards

All implementations must:
- Include validation against official specs
- Document tool capabilities progressively
- Maintain version control of specifications
- Provide examples and troubleshooting
- Follow progressive disclosure principle

## 6. Tool Discovery Reference

> **IMPORTANT FOR CLAUDE CODE:** Before using ANY tool, MCP server, skill, or package, consult these manifests:

### Available Tools Documentation

📋 **MCP Servers:** `docs/tools/mcp-servers.md`
- All installed MCP servers and their tools
- Parameters, returns, costs for each tool
- Examples and validation steps
- **Check this BEFORE calling any `mcp__*` tool**

🎯 **Skills:** `docs/tools/skills.md`
- All installed Claude Code skills
- Trigger keywords and use cases
- Cost breakdown and validation
- **Check this to understand when skills activate**

📦 **Packages:** `docs/tools/packages.md`
- Python packages and system tools
- Purpose and usage for each package
- Dependencies and installation
- **Check this for available capabilities**

### When to Consult Manifests

**Before using a tool:**
1. Read `docs/tools/mcp-servers.md` to understand parameters and costs
2. Check examples to see proper usage
3. Verify tool is listed and documented

**Before activating a skill:**
1. Read `docs/tools/skills.md` to understand triggers
2. Check cost implications
3. Review expected output format

**Before installing packages:**
1. Read `docs/tools/packages.md` to check if already installed
2. Understand purpose and dependencies
3. Follow installation guide if adding new package

---

# Quick Reference: Perplexity MCP Documentation

**This project uses progressive disclosure.** Consult the relevant guide based on your needs:

## 🚀 Getting Started

**New to Perplexity MCP?**
→ See: [`docs/guides/QUICKSTART.md`](docs/guides/QUICKSTART.md)
→ Time: 5 minutes to first search

## 📖 User Guide

**Using Perplexity MCP with Claude Code?**
→ See: [`docs/guides/USER_GUIDE.md`](docs/guides/USER_GUIDE.md)
→ Covers: Examples, tips, output format, integration patterns

## 🔧 Developer Guide

**Building or extending the MCP server?**
→ See: [`docs/guides/DEVELOPER_GUIDE.md`](docs/guides/DEVELOPER_GUIDE.md)
→ Covers: API reference, parameters, costs, project structure

## 💊 Pharma Research

**German pharmaceutical market research?**
→ See: [`docs/guides/PHARMA_RESEARCH.md`](docs/guides/PHARMA_RESEARCH.md)
→ Covers: pharma-research skill v2.0.0, usage, examples, costs

## ⚠️ Troubleshooting

**Encountering issues?**
→ See: [`docs/guides/TROUBLESHOOTING.md`](docs/guides/TROUBLESHOOTING.md)
→ Covers: Common errors, API key issues, installation problems

---

## Additional Resources

### Installation & Setup
→ [`INSTALL.md`](INSTALL.md) - Detailed installation instructions
→ [`README.md`](README.md) - Project overview

### Documentation
→ [`CHANGELOG.md`](CHANGELOG.md) - All changes and updates

### Specifications
→ [`docs/specs/SKILL_SPEC.md`](docs/specs/SKILL_SPEC.md) - SKILL specification
→ [`docs/specs/mcp_research.md`](docs/specs/mcp_research.md) - MCP research notes

---

**Documentation Architecture:** This project follows progressive disclosure principles. Start with high-level guides above, then drill down to tool manifests (`docs/tools/`) and specifications (`docs/specs/`) as needed.

<!-- RESTRUCTURED 2025-11-23: Progressive Disclosure Implementation
Previous version (587 lines) archived at: docs/archive/CLAUDE.md.pre-restructure-2025-11-23

MOVED SECTIONS:
- What This Tool Does → docs/guides/QUICKSTART.md
- Quick Start → docs/guides/QUICKSTART.md
- Natural Language Examples → docs/guides/QUICKSTART.md
- What You Get Back → docs/guides/USER_GUIDE.md
- Tool Parameters → docs/guides/DEVELOPER_GUIDE.md
- Real-World Queries → docs/guides/USER_GUIDE.md
- File Locations → docs/guides/DEVELOPER_GUIDE.md
- Understanding the Output → docs/guides/USER_GUIDE.md
- API Costs → docs/guides/DEVELOPER_GUIDE.md
- Tips & Tricks → docs/guides/USER_GUIDE.md
- Troubleshooting → docs/guides/TROUBLESHOOTING.md
- Integration Examples → docs/guides/USER_GUIDE.md
- Next Steps → docs/guides/QUICKSTART.md
- For Developers → docs/guides/DEVELOPER_GUIDE.md
- Pharma-Research Skill → docs/guides/PHARMA_RESEARCH.md
- Resources → Distributed across guides

Benefits of restructuring:
- 71% reduction in system prompt tokens (587 → 170 lines)
- Clear audience separation (agent vs user vs developer)
- Alignment with Anthropic's progressive disclosure philosophy
- Improved maintainability (single source of truth per topic)
- Zero functional impact on Claude Code agent behavior

Analysis: docs/reports/CLAUDE_MD_PROGRESSIVE_DISCLOSURE_ANALYSIS.md
Implementation: docs/reports/IMPLEMENTATION_PLAN_PROGRESSIVE_DISCLOSURE.md
-->
