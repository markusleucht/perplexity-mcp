# Output Format Documentation

Your Perplexity MCP tools return rich, formatted output with multiple options for consuming the results.

## Response Format

All tools return a **dictionary/JSON object** with the following structure:

```json
{
  "success": true,
  "content": "Plain text response from Perplexity...",
  "citations": ["https://example.com/1", "https://example.com/2"],
  "markdown": "# Search Results\n\n**Query:** ...\n\n## Answer\n\n...",
  "search_type": "pro",
  "file_saved": "/path/to/results.md"
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Whether the search succeeded |
| `content` | string | The raw text response from Perplexity |
| `citations` | array | List of source URLs cited in the response |
| `markdown` | string | Pre-formatted markdown version of results |
| `search_type` | string | Search type used ("pro", "auto", "fast") |
| `search_focus` | string | Search focus (only in social search, value: "social") |
| `file_saved` | string | Path where markdown was saved (if requested) |
| `file_error` | string | Error message if file save failed |
| `error` | string | Error message if search failed |

## Usage Examples

### 1. Get Raw Content Only

```python
result = perplexity_search("What are AI trends in 2025?")
print(result['content'])
# Output: Plain text response suitable for processing
```

### 2. Get Formatted Markdown

```python
result = perplexity_search("What are AI trends in 2025?")
print(result['markdown'])
# Output:
# # Search Results
#
# **Query:** What are AI trends in 2025?
#
# **Search Type:** pro
#
# ## Answer
#
# Agentic AI is leading... (detailed answer)
#
# ## Sources
#
# 1. https://example.com/article1
# 2. https://example.com/article2
```

### 3. Save to File

```python
result = perplexity_search(
    "What are AI trends in 2025?",
    save_to_file="research/ai_trends.md"
)

if result['success']:
    print(f"Saved to: {result['file_saved']}")
    # File created at: research/ai_trends.md
else:
    print(f"Error: {result['error']}")
```

### 4. Access Citations

```python
result = perplexity_search("Latest quantum computing breakthroughs")

print("Sources:")
for i, url in enumerate(result['citations'], 1):
    print(f"{i}. {url}")
```

## Claude Code Usage

### In Claude Code, get markdown directly:

```
Use perplexity_search to research "AI trends 2025" and save to "research.md"
```

Claude Code will:
1. Call the tool with `save_to_file="research.md"`
2. Receive the response dict
3. Extract and display the markdown
4. Optionally save the file

### Claude Code will see:

```
📝 Search Results

Query: AI trends 2025
Search Type: pro

Answer
------

Agentic AI is leading... (formatted text)

Sources
-------

1. https://example.com/article1
2. https://example.com/article2

✓ Saved to: research.md
```

## Markdown Format Structure

The `markdown` field returns formatted output with this structure:

```markdown
# Search Results

**Query:** [Your original query]

**Search Type:** [pro/auto/fast]
[**Search Focus:** social]  # Only for social search

## Answer

[Full response text with proper formatting]

## Sources

1. [URL 1]
2. [URL 2]
3. [URL 3]
...
```

### Example Markdown Output:

```markdown
# Search Results

**Query:** What are the latest AI safety recommendations?

**Search Type:** pro

## Answer

AI safety is increasingly important. Key recommendations include:

- Alignment research focusing on model interpretability
- Robust testing frameworks for large language models
- Multi-stakeholder governance approaches
- Transparency in AI system development

Organizations like OpenAI, Anthropic, and academic institutions are leading this research.

## Sources

1. https://arxiv.org/abs/2023.xxxxx
2. https://openai.com/research/ai-safety
3. https://www.anthropic.com/research
```

## Social Search Output

Social searches include all the same fields, plus:

```json
{
  "success": true,
  "content": "...",
  "citations": [...],
  "markdown": "...",
  "search_focus": "social",
  "file_saved": "social_results.md"
}
```

The markdown for social searches will have:
- Focus on X/Twitter and Reddit discussions
- Emphasis on community insights
- Real-time conversation trends

## File Saving

When you specify `save_to_file`:

```python
result = perplexity_social(
    "What's the latest discussion about Web3?",
    save_to_file="web3_discussions.md"
)
```

The tool will:
1. Create directories if they don't exist
2. Write the markdown content to the file
3. Return `file_saved` with the path
4. Return `file_error` if anything went wrong

## Accessing Results in Code

### Using the Raw Content:
```python
# Process the raw content
text = result['content']
# Use for further processing, summarization, etc.
```

### Using the Markdown:
```python
# Get pre-formatted markdown
md = result['markdown']
# Save it directly
with open("output.md", "w") as f:
    f.write(md)
```

### Using Citations:
```python
# Access just the sources
sources = result['citations']
for source in sources:
    print(f"Source: {source}")
```

## Error Handling

When a search fails:

```python
result = perplexity_search("query")

if result['success']:
    print("Search succeeded!")
    print(result['markdown'])
else:
    print(f"Error: {result['error']}")
```

Common error messages:
- `"OpenAI package not installed..."` - Dependencies need to be installed
- `"Invalid API key"` - Check your `.env` file
- `"Rate limit exceeded"` - Wait before next request or upgrade plan
- `"File error: [details]"` - Permission or path issue when saving

## Tips

1. **For Reading**: Use `content` field for machine processing
2. **For Sharing**: Use `markdown` field for human-readable format
3. **For Storage**: Use `save_to_file` parameter to persist results
4. **For Attribution**: Use `citations` field to credit sources
5. **For Integration**: Check `success` field before processing results

## Compatibility

The output format is:
- ✅ JSON/Dict compatible - can be easily serialized
- ✅ Markdown compatible - renders in all markdown viewers
- ✅ Claude Code compatible - understood by Claude's tools
- ✅ Python compatible - works with any Python processor
- ✅ Shell compatible - can be piped through jq for JSON parsing
