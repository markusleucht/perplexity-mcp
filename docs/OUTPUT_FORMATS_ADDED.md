# Output Format Enhancements - Summary

Your Perplexity MCP tools now support rich output formats with markdown generation and automatic file saving.

## What Changed

### 1. Enhanced Response Structure

Each tool now returns:

```python
{
    "success": True,
    "content": "Raw text answer",
    "citations": ["url1", "url2"],
    "markdown": "# Formatted markdown version",
    "search_type": "pro",
    "file_saved": "/path/to/file.md" # If save_to_file was used
}
```

### 2. New Functions

**`format_to_markdown()`** - Converts search results to beautiful markdown

```python
markdown = format_to_markdown(
    query="Your question",
    content="Answer text",
    citations=["url1", "url2"],
    search_type="pro",
    search_focus=None  # or "social"
)
```

Returns pre-formatted markdown like:
```markdown
# Search Results

**Query:** Your question

**Search Type:** pro

## Answer

Answer text here...

## Sources

1. url1
2. url2
```

### 3. New Parameters

Both tools now accept:

| Parameter | Type | Purpose |
|-----------|------|---------|
| `save_to_file` | string | Path to save markdown (e.g., "results.md") |

Example:
```python
result = perplexity_search(
    query="Your query",
    save_to_file="research.md"  # NEW
)
```

### 4. Updated Tool Definitions

MCP tools now include `save_to_file` parameter in their schema, making it available in Claude Code.

---

## Usage Examples

### Example 1: Get Markdown

```python
result = perplexity_search("What are AI trends in 2025?")

# Access markdown
print(result['markdown'])

# Or save it
with open("output.md", "w") as f:
    f.write(result['markdown'])
```

### Example 2: Auto-Save to File

```python
result = perplexity_search(
    "What are AI trends in 2025?",
    save_to_file="ai_trends_2025.md"
)

if result.get('file_saved'):
    print(f"✓ Saved to {result['file_saved']}")
    # File created automatically at: ai_trends_2025.md
```

### Example 3: In Claude Code

Just ask naturally:
```
Search for quantum computing breakthroughs and save to quantum.md
```

Claude Code will:
1. Call with `save_to_file="quantum.md"`
2. Show you the formatted markdown
3. Create the file automatically

### Example 4: Process Different Parts

```python
result = perplexity_search("query")

# Get raw content for processing
raw_text = result['content']

# Get formatted markdown for sharing
markdown = result['markdown']

# Get sources for citations
sources = result['citations']
```

---

## Markdown Format Details

The markdown output follows this structure:

```markdown
# Search Results

**Query:** [your search query]

**Search Type:** [pro/auto/fast]
[**Search Focus:** [social] - only for social searches]

## Answer

[Full formatted answer with:
- Proper paragraphs
- Bullet points preserved
- Lists formatted
- Code blocks if any]

## Sources

1. [First source URL]
2. [Second source URL]
3. [Additional sources...]
```

### Example Output:

```markdown
# Search Results

**Query:** Latest developments in quantum computing

**Search Type:** pro

## Answer

Recent advances in quantum computing in 2025 include:

- Development of error-corrected quantum computers
- Progress in quantum teleportation over longer distances
- New quantum algorithms for practical applications
- Increased quantum processor qubit counts

Major tech companies and research institutions continue leading this field.

## Sources

1. https://arxiv.org/abs/quantum-2025-001
2. https://www.quantumcomputing.com/news/2025
3. https://research.ibm.com/quantum-2025
```

---

## File Saving Details

When using `save_to_file` parameter:

**Features:**
- ✅ Automatically creates directories if needed
- ✅ Overwrites existing files (idempotent)
- ✅ Returns success/error status
- ✅ Saves full markdown automatically

**Example:**
```python
result = perplexity_social(
    "What's trending on Twitter about AI?",
    save_to_file="social_trends/ai_nov2025.md"
)

# Directories auto-created: social_trends/
# File saved: social_trends/ai_nov2025.md
# Response includes: file_saved, or file_error if failed
```

---

## Response Fields Reference

### New/Updated Fields:

| Field | Type | When Present | Notes |
|-------|------|---|---|
| `markdown` | string | always (if success=true) | Pre-formatted markdown version |
| `save_to_file` | (input only) | - | Parameter for requesting file save |
| `file_saved` | string | when file saved successfully | Path where file was saved |
| `file_error` | string | when file save fails | Error message for save failure |

### Existing Fields (unchanged):

| Field | Type | Notes |
|-------|------|---|
| `success` | boolean | True if search succeeded |
| `content` | string | Raw text response |
| `citations` | list | Source URLs |
| `search_type` | string | Type used (pro/auto/fast) |
| `search_focus` | string | Only in social: "social" |
| `error` | string | Only if success=false |

---

## Migration Notes

### For Existing Code

If you were already using the tools, nothing breaks:

```python
# Old code still works
result = perplexity_search("query")
print(result['content'])  # Still works
```

### New Features Added

```python
# New features available
print(result['markdown'])  # NEW - formatted output

# New parameter
result = perplexity_search(
    "query",
    save_to_file="output.md"  # NEW - auto-save
)
```

---

## For Claude Code Users

Claude Code automatically:

1. ✅ Uses the `save_to_file` parameter when you ask
2. ✅ Displays the formatted markdown beautifully
3. ✅ Creates the file automatically
4. ✅ Shows you the file path

**Example interaction:**
```
You: "Search for Python security updates and save to python_security.md"

Claude Code:
  → Calls perplexity_search with save_to_file="python_security.md"
  → Displays the formatted markdown
  → Shows: "✓ Saved to python_security.md"
```

---

## Use Case Examples

### 1. Research Documentation

```python
result = perplexity_search(
    "Best practices for microservices architecture",
    save_to_file="docs/microservices_best_practices.md"
)

# File created ready for documentation
```

### 2. Meeting Notes

```python
result = perplexity_search(
    "Summary of recent cybersecurity conferences",
    save_to_file="meeting_notes/security_2025.md"
)

# Formatted file ready to share with team
```

### 3. Social Media Analysis

```python
result = perplexity_social(
    "Latest discussions about blockchain scalability",
    save_to_file="research/blockchain_discussion.md"
)

# Social media insights in structured format
```

### 4. Processing Pipeline

```python
result = perplexity_search("Your query")

# Extract parts for different uses
raw = result['content']          # For processing
markdown = result['markdown']    # For sharing
sources = result['citations']   # For citations

# Use in pipeline
process(raw)
share(markdown)
cite(sources)
```

---

## Error Handling

### File Save Errors

If file save fails, you still get the search results:

```python
result = perplexity_search(
    "query",
    save_to_file="/restricted/path.md"  # No permission
)

if result['success']:
    # Search succeeded
    print(result['content'])

    if result.get('file_error'):
        # But file save failed
        print(f"File save error: {result['file_error']}")
```

### Check Before Using

```python
result = perplexity_search("query")

if not result['success']:
    print(f"Search failed: {result['error']}")
else:
    # Safe to use all fields
    print(result['markdown'])
    print(result['citations'])
```

---

## Performance Notes

- ✅ Markdown generation is fast (no API calls)
- ✅ File operations are quick (I/O only)
- ✅ No additional API cost for markdown
- ✅ No additional API cost for file saving

---

## Backward Compatibility

✅ **100% backward compatible**

- Old response fields unchanged
- New fields are additions only
- No parameters required
- Existing code continues working

---

## Summary of Changes

| What | Before | After | Benefit |
|-----|--------|-------|---------|
| Output format | Dict only | Dict + Markdown | Easy sharing |
| File saving | Manual | Automatic | Convenience |
| Markdown | Not available | Built-in | Ready to use |
| Parameter options | Basic | Extended | More control |

---

## Next Steps

1. **Try the markdown output:**
   ```python
   result = perplexity_search("query")
   print(result['markdown'])
   ```

2. **Try auto-saving:**
   ```python
   result = perplexity_search("query", save_to_file="output.md")
   ```

3. **Use in Claude Code:**
   Just ask naturally and it works!

---

## Documentation

For complete details, see:
- **`OUTPUT_SUMMARY.md`** - Overview and patterns
- **`OUTPUT_FORMAT.md`** - Detailed field reference
- **`OUTPUT_EXAMPLES.md`** - Real-world examples
- **`DOCS.md`** - Documentation index
