# Documentation Index

Complete guide to your Perplexity MCP Server setup and usage.

## 📚 Start Here

**New to this project?** Start with one of these:

1. **`QUICKSTART.md`** - Get running in 5 minutes
2. **`OUTPUT_SUMMARY.md`** - Understand what you get back

---

## 📖 Full Documentation

### Setup & Configuration
- **`SETUP_COMPLETE.md`** - System upgrade and installation recap
- **`CLAUDE_CODE_MCP.md`** - How to use with Claude Code
- **`README.md`** - Project overview and features
- **`docs/plan/plan.md`** - Original implementation plan

### Output & Usage
- **`OUTPUT_SUMMARY.md`** ⭐ - **START HERE** - Output overview and patterns
- **`OUTPUT_FORMAT.md`** - Detailed field descriptions and API reference
- **`OUTPUT_EXAMPLES.md`** - Real examples and use cases

### Configuration Files
- **`.mcp.json`** - MCP server definition (for Claude Code)
- **`.claude/settings.json`** - MCP server enablement
- **`.env`** - API key (keep secret!)
- **`.env.example`** - Template for API key

---

## 🎯 Quick Answers

### "What does the tool return?"
→ See **`OUTPUT_SUMMARY.md`** (2 min read)

### "Can I get markdown output?"
→ Yes! See **`OUTPUT_EXAMPLES.md`** for examples

### "How do I save to a file?"
→ Use `save_to_file` parameter. See **`OUTPUT_FORMAT.md`**

### "How do I use this with Claude Code?"
→ See **`CLAUDE_CODE_MCP.md`** - already configured!

### "What's my API quota?"
→ You have $5. See **`QUICKSTART.md`** Cost Tracking section

### "How do I activate the virtual environment?"
→ Run: `source venv/bin/activate`

---

## 🔍 Find By Task

### I want to...

**Run a search from command line**
```bash
source venv/bin/activate
python src/perplexity_mcp.py
```
→ See `QUICKSTART.md` Section 3

**Use with Claude Code**
- It's already configured!
- Just ask Claude Code naturally
→ See `CLAUDE_CODE_MCP.md`

**Save results to markdown file**
```python
result = perplexity_search("query", save_to_file="output.md")
```
→ See `OUTPUT_FORMAT.md` Example 3

**Get just the text content**
```python
text = result['content']
```
→ See `OUTPUT_EXAMPLES.md` Example 6

**Get formatted markdown**
```python
md = result['markdown']
```
→ See `OUTPUT_EXAMPLES.md` Example 6

**Access source citations**
```python
sources = result['citations']
```
→ See `OUTPUT_FORMAT.md` Accessing Citations

**Search social media (X/Twitter, Reddit)**
```python
result = perplexity_social("query")
```
→ See `OUTPUT_EXAMPLES.md` Example 2

**Check if search succeeded**
```python
if result['success']:
    # use result
```
→ See `OUTPUT_FORMAT.md` Error Handling

**Monitor API costs**
→ Check dashboard at https://www.perplexity.ai/settings/api

**Set up in another project**
→ Copy `.mcp.json` and `.claude/settings.json`

---

## 📊 File Structure

```
/Users/markus/perplexity/
├── 📄 DOCS.md                    ← You are here
├── 📄 QUICKSTART.md              ← Start here
├── 📄 OUTPUT_SUMMARY.md          ← Understanding outputs
├── 📄 OUTPUT_FORMAT.md           ← Detailed reference
├── 📄 OUTPUT_EXAMPLES.md         ← Real examples
├── 📄 CLAUDE_CODE_MCP.md         ← Claude Code setup
├── 📄 SETUP_COMPLETE.md          ← Installation recap
├── 📄 README.md                  ← Project overview
│
├── 🔧 .mcp.json                  ← MCP server config
├── 🔧 .claude/settings.json      ← Enable MCP server
├── 🔧 .env                       ← Your API key
├── 🔧 .env.example               ← API key template
├── 🔧 .gitignore                 ← Git ignore rules
├── 🔧 pyproject.toml             ← Python dependencies
│
├── 🐍 src/
│   ├── __init__.py
│   └── perplexity_mcp.py         ← Main MCP server (~300 lines)
│
├── 🔐 venv/                      ← Virtual environment (Python 3.12)
│   └── lib/python3.12/site-packages/
│       ├── openai/               ← Perplexity client
│       ├── python_dotenv/        ← Environment variables
│       └── mcp/                  ← Model Context Protocol
│
└── 📁 docs/
    └── plan/
        └── plan.md              ← Original implementation plan
```

---

## 🚀 Getting Started (30 seconds)

1. **Activate venv:**
   ```bash
   cd /Users/markus/perplexity
   source venv/bin/activate
   ```

2. **Test it:**
   ```bash
   python src/perplexity_mcp.py
   ```

3. **Use it:**
   - In Python: Import from `src.perplexity_mcp`
   - In Claude Code: Just ask naturally!

---

## 📝 Common Searches in Docs

| Looking for... | File | Section |
|---|---|---|
| How to use | `QUICKSTART.md` | All sections |
| Output format | `OUTPUT_SUMMARY.md` | Quick Reference |
| Response fields | `OUTPUT_FORMAT.md` | Response Fields |
| Examples | `OUTPUT_EXAMPLES.md` | All examples |
| Claude Code | `CLAUDE_CODE_MCP.md` | Using It section |
| API costs | `QUICKSTART.md` | Cost Tracking |
| Error handling | `OUTPUT_FORMAT.md` | Error Handling |
| File saving | `OUTPUT_FORMAT.md` | File Saving |
| System info | `SETUP_COMPLETE.md` | System Info |

---

## 🔗 External Links

- **Perplexity API Dashboard**: https://www.perplexity.ai/settings/api
- **Perplexity Docs**: https://docs.perplexity.ai
- **Claude Code Guide**: Available in Claude Code with `/help`

---

## ✅ Verification Checklist

Everything is set up! Verify with:

- ✅ `.env` has your API key
- ✅ `venv/` directory exists with Python 3.12
- ✅ `.mcp.json` defines the server
- ✅ `.claude/settings.json` enables it for Claude Code
- ✅ `src/perplexity_mcp.py` is the implementation
- ✅ All documentation files exist

---

## 💡 Pro Tips

1. **Always activate venv first**: `source venv/bin/activate`
2. **Check success before using results**: `if result['success']:`
3. **Use markdown for sharing**: `result['markdown']` is pre-formatted
4. **Use content for processing**: `result['content']` is plain text
5. **Save while searching**: Use `save_to_file` parameter
6. **Monitor costs**: Check API dashboard weekly

---

## 🆘 Need Help?

**Problem** | **Solution**
---|---
Tool not found | Check `.mcp.json` exists, Claude Code is reloaded
API key error | Check `.env` has valid key from https://perplexity.ai/settings/api
Permission error | Check venv is activated: `which python`
Rate limit | Wait 60 seconds or check API dashboard
File save fails | Check directory permissions

---

## 📞 Support Resources

- **This documentation**: All .md files in this directory
- **Claude Code help**: Type `/help` in Claude Code
- **Perplexity API docs**: https://docs.perplexity.ai
- **Python documentation**: Check docstrings with `help(perplexity_search)`

---

**Last Updated**: 2025-11-22
**Setup**: Python 3.12.12 | pip 25.3 | macOS
**API Status**: $5 credits available
