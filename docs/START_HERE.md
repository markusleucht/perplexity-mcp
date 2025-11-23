# 🚀 START HERE - Perplexity MCP Server

Your Perplexity AI MCP server is fully configured and ready to use!

## ⚡ Quick Start (30 seconds)

### 1. Activate Virtual Environment
```bash
cd /Users/markus/perplexity
source venv/bin/activate
```

### 2. Test It
```bash
python src/perplexity_mcp.py
```

### 3. Use It
- **In Python:** Import `perplexity_search` and `perplexity_social`
- **In Claude Code:** Just ask naturally!

---

## 📋 What You Get

Every search returns:

```python
{
    "success": True,           # Did it work?
    "content": "...",         # Raw answer text
    "markdown": "# ...",      # Formatted markdown (READY TO SAVE!)
    "citations": ["url1"],    # Source URLs
    "file_saved": "path.md"   # If you requested save
}
```

### Three Ways to Use Output:

1. **Get formatted markdown** → Share or save to .md file
   ```python
   print(result['markdown'])
   ```

2. **Get raw content** → Process or analyze
   ```python
   print(result['content'])
   ```

3. **Get sources** → Create bibliography
   ```python
   print(result['citations'])
   ```

---

## 🎯 Common Tasks

### Search & Get Markdown
```python
result = perplexity_search("What are the latest AI trends?")
print(result['markdown'])
```

### Search & Save to File
```python
result = perplexity_search(
    "What are the latest AI trends?",
    save_to_file="ai_trends.md"
)
# File automatically created!
```

### Social Media Search
```python
result = perplexity_social("What's trending about AI?")
print(result['markdown'])
```

### In Claude Code
Just ask:
```
Search for quantum computing and save to quantum.md
```
Claude Code handles everything! ✨

---

## 📚 Documentation

| Need | File | Time |
|------|------|------|
| **Output formats** | `OUTPUT_SUMMARY.md` ⭐ | 5 min |
| **Real examples** | `OUTPUT_EXAMPLES.md` | 10 min |
| **Detailed reference** | `OUTPUT_FORMAT.md` | Reference |
| **All docs** | `DOCS.md` | Index |
| **Claude Code setup** | `CLAUDE_CODE_MCP.md` | Already done! |

---

## 💡 Key Features

✅ **Markdown output** - Pre-formatted, ready to share
✅ **Auto file save** - `save_to_file="name.md"` parameter
✅ **Citations included** - Full source attribution
✅ **Claude Code ready** - Just ask naturally
✅ **Fast** - Markdown generation instant
✅ **Error handling** - Graceful failure modes
✅ **Backward compatible** - Old code still works

---

## 🔍 Understanding the Response

### Success Response:
```python
result = perplexity_search("query")

result['success']      # True
result['content']      # Plain text answer
result['markdown']     # Formatted markdown (use this!)
result['citations']    # ["url1", "url2", ...]
result['search_type']  # "pro", "auto", or "fast"
```

### Error Response:
```python
result = perplexity_search("query")

result['success']      # False
result['error']        # Error message
result['content']      # None
result['citations']    # []
```

### With File Save:
```python
result = perplexity_search("query", save_to_file="out.md")

result['file_saved']   # "/full/path/to/out.md"
# or
result['file_error']   # If save failed
```

---

## 💻 System Info

```
Python:    3.12.12 (Homebrew)
pip:       25.3
OS:        macOS
Location:  /opt/homebrew/bin/python3.12
Venv:      /Users/markus/perplexity/venv/
API Key:   In .env (never commit!)
```

---

## 🎓 Learning Path

### Beginner (10 min)
1. Read `OUTPUT_SUMMARY.md`
2. Run the test: `python src/perplexity_mcp.py`
3. Try a search in Python

### Intermediate (20 min)
1. Read `OUTPUT_EXAMPLES.md`
2. Try different search types
3. Try saving to file
4. Try using in Claude Code

### Advanced (30 min)
1. Read `OUTPUT_FORMAT.md`
2. Read `CLAUDE_CODE_MCP.md`
3. Integrate into your workflow

---

## 🚨 Common Issues

### "PERPLEXITY_API_KEY not set"
Check `.env` has your key:
```bash
cat .env
# Should show: PERPLEXITY_API_KEY=pplx-...
```

### "No results returned"
- Check API has credits: https://www.perplexity.ai/settings/api
- Try different search_type: `search_type="auto"`
- Rephrase your query

### "File not saving"
- Check directory permissions
- Try relative path: `save_to_file="output.md"`

---

## 💰 API Costs

- **You have:** $5 in credits
- **Pro search:** $0.20-$0.50 per query
- **Social search:** $0.10-$0.20 per query
- **Estimated:** 25-50 searches per month
- **Monitor:** https://www.perplexity.ai/settings/api

---

## 🔗 Integration Points

### With Python Projects
```python
from src.perplexity_mcp import perplexity_search

# Use anywhere
result = perplexity_search("query")
```

### With Claude Code
Already configured! Just ask naturally:
```
"Search for X and save to result.md"
```

### With Shell Scripts
```bash
source venv/bin/activate
python -c "from src.perplexity_mcp import perplexity_search; ..."
```

---

## ✅ Your Setup Includes

- ✅ Python 3.12 with pip 25.3
- ✅ Virtual environment with dependencies
- ✅ MCP server implementation (~300 lines)
- ✅ Claude Code integration
- ✅ Comprehensive documentation
- ✅ Working API key in .env
- ✅ Markdown output generation
- ✅ Automatic file saving

---

## 🎯 Next Steps

1. **Now:** Read `OUTPUT_SUMMARY.md` (5 min)
2. **Then:** Try a search in Claude Code
3. **Then:** Try `save_to_file` parameter
4. **Then:** Use in your projects!

---

## 📖 Quick Links

- **All Documentation:** `DOCS.md`
- **Output Formats:** `OUTPUT_SUMMARY.md` ⭐
- **Examples:** `OUTPUT_EXAMPLES.md`
- **Claude Code:** `CLAUDE_CODE_MCP.md`
- **Detailed Reference:** `OUTPUT_FORMAT.md`

---

## 💬 Questions?

Check these files first:
- `QUICKSTART.md` - Common questions
- `OUTPUT_SUMMARY.md` - Output questions
- `CLAUDE_CODE_MCP.md` - Claude Code questions
- `DOCS.md` - Find by topic

---

**You're all set! Start with `OUTPUT_SUMMARY.md` now.** 🚀
