# Pharma-Research Skill: GitHub Portability ✅

**Date:** 2025-11-23
**Status:** Published to GitHub - Truly Portable

---

## ✅ What Was Done

### 1. Verified Skill Portability

**Checked for local dependencies:**
- ✅ No hardcoded local paths (no `/Users/markus/...`)
- ✅ No hardcoded user directories (no `~/.claude/...`)
- ✅ Generic MCP tool references: `perplexity_search` and `perplexity_social`
- ✅ Works on any machine with Perplexity MCP configured

### 2. Created GitHub Repository

**Repository:** https://github.com/markusleucht/claude-code-skills

**Contents:**
```
claude-code-skills/
├── README.md                    # Setup instructions and prerequisites
├── .gitignore                   # Git ignore patterns
└── pharma-research/
    ├── SKILL.md                 # Main skill definition (350 lines)
    └── references/
        └── query-strategies.md  # Query formulation guidance
```

### 3. Published to GitHub

**Commit:** `8415b10` - "Add pharma-research skill for German pharmaceutical market analysis"

**Branch:** `master`

**Status:** ✅ Pushed successfully

---

## 🚀 How to Use on Another Machine

### Prerequisites

1. **Perplexity MCP Server** must be configured on the new machine
2. **Claude Code** must be installed
3. **Git** must be installed

### Installation Steps

```bash
# 1. Clone the skills repository
git clone https://github.com/markusleucht/claude-code-skills.git

# 2a. Install to user-level (available everywhere)
cp -r claude-code-skills/pharma-research ~/.claude/skills/

# OR

# 2b. Install to project-level (specific project only)
cp -r claude-code-skills/pharma-research /your/project/.claude/skills/

# 3. Restart Claude Code to load the skill
```

### Verify Installation

```bash
# Check skill is installed
ls -la ~/.claude/skills/pharma-research/

# Should see:
# - SKILL.md
# - references/query-strategies.md
```

---

## 🔧 Perplexity MCP Setup (Required)

The skill requires Perplexity MCP server on each machine. Setup:

### 1. Install Perplexity MCP

```bash
# In your project directory
mkdir -p src
# Copy your perplexity_mcp.py to src/
```

### 2. Configure .mcp.json

Create `.mcp.json` in project root:

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "python3",
      "args": ["src/perplexity_mcp.py"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-key-here"
      }
    }
  }
}
```

### 3. Test MCP Tools

In Claude Code, verify tools are available:
- `perplexity_search` - Pro Search with web crawling
- `perplexity_social` - Social media search

---

## ✅ Portability Checklist

- [x] **No hardcoded paths** - Skill uses generic tool names
- [x] **No local dependencies** - Only requires standard Perplexity MCP
- [x] **Git version controlled** - Can be cloned to any machine
- [x] **Documentation included** - README explains prerequisites
- [x] **Private repository** - Your skills remain private
- [x] **Progressive disclosure** - References loaded as needed
- [x] **Validated structure** - Passed skill-creator validation

---

## 📦 What's in the GitHub Repo

### README.md

- Overview of available skills
- Installation instructions
- Perplexity MCP prerequisites
- Usage examples

### pharma-research/SKILL.md

**350 lines covering:**
1. When to use the skill (trigger scenarios)
2. Core research framework (epidemiology, competition, market access)
3. Research methodology (query formulation, Perplexity integration)
4. Output structure (business report format)
5. Quality standards (data validation, source hierarchy)
6. Tips and examples

**Key Design:**
- Guides methodology without constraining Perplexity
- No hardcoded examples that become outdated
- Flexible for any indication-medication pair

### pharma-research/references/query-strategies.md

**Strategic guidance for:**
- Effective German pharma query patterns
- Search sequencing strategies
- Source-specific patterns
- Common pitfalls to avoid

**Progressive disclosure:**
- Only loaded when Claude needs deeper query guidance
- Keeps main context efficient

---

## 🔄 Updating the Skill

### Making Changes

```bash
# 1. Edit skill files locally
cd ~/.claude/skills/pharma-research
# Make changes to SKILL.md or references/

# 2. Test changes in Claude Code

# 3. Commit and push to GitHub
cd ~/.claude/skills
git add pharma-research/
git commit -m "Update: [describe changes]"
git push origin master
```

### Pulling Updates on Another Machine

```bash
# 1. Pull latest from GitHub
cd ~/claude-code-skills
git pull origin master

# 2. Update installed skill
cp -r pharma-research ~/.claude/skills/

# 3. Restart Claude Code
```

---

## 🎯 Verification

### Skill Works Portably Because:

1. **Generic Tool References**
   - Uses `perplexity_search` (not `mcp__perplexity__search`)
   - Works with any MCP server that provides these tools
   - No hardcoded connection strings

2. **No Environment Assumptions**
   - No paths like `/Users/markus/...`
   - No assumptions about directory structure
   - Works in `~/.claude/skills/` or `.claude/skills/`

3. **Self-Contained**
   - All instructions in SKILL.md
   - References are optional enhancements
   - No external dependencies beyond Perplexity MCP

4. **Documentation Included**
   - README explains prerequisites
   - Clear installation steps
   - MCP setup instructions

---

## 📊 Repository Structure

```
https://github.com/markusleucht/claude-code-skills
│
├── README.md              # Main documentation
├── .gitignore            # Ignore patterns
│
└── pharma-research/      # Skill directory
    ├── SKILL.md          # Main skill (portable)
    └── references/
        └── query-strategies.md  # Optional guidance
```

**Future skills** can be added as siblings to `pharma-research/`:
```
├── clinical-trials-research/
├── health-economics/
└── regulatory-intel/
```

---

## 🔐 Security Notes

**Repository is PRIVATE:**
- Only you can access it
- Skills contain your research methodology
- No API keys stored in repo (they go in `.env` files)

**To share with team:**
```bash
# Add collaborators on GitHub
gh repo invite-collaborator markusleucht/claude-code-skills @username
```

---

## 💡 Best Practices

### For Skill Development

1. **Develop locally** in `~/.claude/skills/pharma-research/`
2. **Test thoroughly** with real queries
3. **Commit to git** regularly
4. **Push to GitHub** when stable
5. **Document changes** in commit messages

### For Multiple Machines

1. **Clone once** on each machine: `git clone https://github.com/markusleucht/claude-code-skills.git`
2. **Copy to skills directory** (user or project level)
3. **Pull updates** periodically: `git pull origin master`
4. **Keep MCP config** in sync across machines

### For Team Collaboration

1. **Share repository** with team members
2. **Use branches** for experimental changes
3. **Review changes** before merging to master
4. **Version tag** stable releases: `git tag v1.0.0`

---

## 📝 Quick Reference

### Clone on New Machine
```bash
git clone https://github.com/markusleucht/claude-code-skills.git
cp -r claude-code-skills/pharma-research ~/.claude/skills/
```

### Update Skill
```bash
cd ~/.claude/skills
git pull origin master
cp -r claude-code-skills/pharma-research ~/.claude/skills/
```

### Verify Portability
```bash
# Check for hardcoded paths (should return nothing)
grep -r "/Users/markus" ~/.claude/skills/pharma-research/
grep -r "~/.claude" ~/.claude/skills/pharma-research/
```

---

## ✅ Completion Status

- [x] GitHub repository created
- [x] Skill published to GitHub
- [x] README documentation added
- [x] Portability verified (no local dependencies)
- [x] Installation instructions documented
- [x] Unnecessary zip file deleted
- [x] Project documentation updated

---

**The skill is now truly portable and can be installed on any machine with Claude Code and Perplexity MCP!** 🎉

**GitHub URL:** https://github.com/markusleucht/claude-code-skills
