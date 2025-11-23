# Output Format Summary

Your Perplexity MCP tools support multiple output formats for maximum flexibility.

## Quick Reference

### What You Get

Every search returns:

```
✓ Raw Content    → Plain text answer
✓ Markdown       → Formatted, shareable version
✓ Citations      → Source URLs
✓ Metadata       → Search type, success status
✓ File Save      → Optional automatic .md file creation
```

### Response Structure

```python
{
    "success": True/False,           # Did it work?
    "content": "...",               # Raw answer text
    "citations": ["url1", "url2"],  # Source links
    "markdown": "# Title\n\n...",   # Formatted MD
    "search_type": "pro",           # Type used
    "file_saved": "path.md"         # If saved to file
}
```

---

## Three Ways to Use Output

### 1️⃣ Get the Markdown (Best for Claude Code)

```python
result = perplexity_search("query")
md = result['markdown']

# Use it directly in Claude Code
# It displays beautifully and can be saved to files
```

**Best for:**
- Sharing results
- Reading comprehension
- Documentation
- Saving to `.md` files
- Viewing in markdown viewers

---

### 2️⃣ Get Raw Content (Best for Processing)

```python
result = perplexity_search("query")
text = result['content']

# Process, summarize, analyze, or transform
```

**Best for:**
- Further processing
- Feeding to other AI models
- Data extraction
- Machine processing

---

### 3️⃣ Automatic File Save (Best for Storage)

```python
result = perplexity_search(
    "query",
    save_to_file="results.md"
)

# File automatically created: results.md
# Full markdown already formatted and saved
```

**Best for:**
- Persistent storage
- Team collaboration
- Knowledge bases
- Research archives

---

## In Claude Code

You can ask naturally:

```
"Search for the latest Python security updates and save as python_security.md"
```

Claude Code will:
1. Call `perplexity_search()` with `save_to_file="python_security.md"`
2. Receive the response dict
3. Display the markdown beautifully
4. Save the file to your project

---

## Markdown Format

The `markdown` field is always formatted like this:

```markdown
# Search Results

**Query:** What were you searching for

**Search Type:** pro/auto/fast

## Answer

[Formatted answer with paragraphs, lists, etc.]

## Sources

1. URL 1
2. URL 2
3. URL 3
```

This is:
- ✅ Readable in any text editor
- ✅ Renders beautifully on GitHub
- ✅ Compatible with Obsidian, Notion, etc.
- ✅ Easily convertible to HTML, PDF
- ✅ Version-control friendly

---

## Citation Handling

```python
result = perplexity_search("query")

# Get citations
sources = result['citations']
# Returns: ["https://source1.com", "https://source2.com", ...]

# Or use the formatted version in markdown
# Already includes numbered sources
```

---

## File Operations

### Create Markdown File

```python
result = perplexity_search(
    "your query",
    save_to_file="research/topic.md"
)

if result.get('file_saved'):
    print(f"✓ Saved to {result['file_saved']}")
else:
    print(f"✗ Error: {result.get('file_error')}")
```

### Supported Paths

```python
# Relative path (created in current directory)
save_to_file="results.md"

# Nested path (directories auto-created)
save_to_file="research/2025/ai_trends.md"

# Absolute path
save_to_file="/Users/markus/perplexity/output.md"

# Home directory
save_to_file="~/projects/research.md"  # Requires expansion
```

---

## Response Fields Explained

| Field | Type | Always Present | Notes |
|-------|------|---|---|
| `success` | bool | ✓ | False if API error or search failed |
| `content` | str | ✓ | Null if failed; plain text when successful |
| `citations` | list | ✓ | Empty list if no citations found |
| `markdown` | str | ✓* | Null if search failed |
| `search_type` | str | ✓* | "pro", "auto", or "fast" |
| `search_focus` | str | ✗ | Only present for social searches ("social") |
| `file_saved` | str | ✗ | Only present if file successfully saved |
| `file_error` | str | ✗ | Only present if file save failed |
| `error` | str | ✗ | Only present if search failed |

*When success=True

---

## Common Patterns

### Pattern 1: Check → Extract → Use

```python
result = perplexity_search("query")

if result['success']:
    print(result['markdown'])  # Display

    # Or save manually
    with open("out.md", "w") as f:
        f.write(result['markdown'])
else:
    print(f"Error: {result['error']}")
```

### Pattern 2: Automatic Save

```python
result = perplexity_search(
    "query",
    save_to_file="output.md"
)

# File is already saved
# No manual file handling needed
```

### Pattern 3: Process the Content

```python
result = perplexity_search("query")

# Work with raw content
text = result['content']
lines = text.split('\n')

# Filter, process, transform
filtered = [l for l in lines if 'important' in l]
```

### Pattern 4: Use Everything

```python
result = perplexity_search("query", save_to_file="out.md")

# Get multiple views
raw = result['content']
formatted = result['markdown']
sources = result['citations']
filepath = result.get('file_saved')

# Use in different contexts
```

---

## Tips & Tricks

### 💾 Save While You Search
```python
result = perplexity_search(
    "topic",
    save_to_file="research/topic.md"  # Saves automatically
)
```

### 📋 Always Check Success First
```python
if result['success']:
    # Safe to use result['content'], etc.
    pass
```

### 🔗 Extract URLs for Bibliography
```python
sources = result['citations']
for i, url in enumerate(sources, 1):
    print(f"[{i}]: {url}")
```

### 📝 Get Markdown Ready to Share
```python
result = perplexity_search("query")
md = result['markdown']
# Ready to post, share, or save - no formatting needed!
```

### ⚡ Fast Processing with Raw Content
```python
result = perplexity_search("query", search_type="fast")
text = result['content']
# Quick answer for further processing
```

---

## Error Cases

### API Error
```json
{
  "success": false,
  "error": "Rate limit exceeded",
  "content": null,
  "citations": []
}
```

### File Save Error
```json
{
  "success": true,
  "content": "...",
  "markdown": "...",
  "file_error": "Permission denied: /restricted/path.md"
}
```
(Note: Search succeeded but file save failed)

### Missing API Key
```json
{
  "success": false,
  "error": "PERPLEXITY_API_KEY not set in .env",
  "content": null,
  "citations": []
}
```

---

## Complete Example

```python
from src.perplexity_mcp import perplexity_search

# Perform search with file save
result = perplexity_search(
    query="Latest developments in quantum computing",
    search_type="pro",
    max_tokens=1024,
    save_to_file="quantum_research_2025.md"
)

# Check success
if not result['success']:
    print(f"Search failed: {result['error']}")
    exit(1)

# Access different formats
print("=== Raw Content ===")
print(result['content'][:200] + "...\n")

print("=== Sources ===")
for i, url in enumerate(result['citations'], 1):
    print(f"{i}. {url}")

print("=== File Status ===")
if result.get('file_saved'):
    print(f"✓ Saved to {result['file_saved']}")
else:
    print(f"✗ File save failed: {result.get('file_error')}")

# Get markdown for sharing
markdown_content = result['markdown']
```

---

## Documentation Files

For more details, see:
- **`OUTPUT_FORMAT.md`** - Detailed field descriptions
- **`OUTPUT_EXAMPLES.md`** - Real output examples
- **`QUICKSTART.md`** - Quick reference
- **`CLAUDE_CODE_MCP.md`** - Claude Code integration
