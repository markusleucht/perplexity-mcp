# Output Examples

Here are real examples of what the tools return.

## Example 1: Pro Search Response

### Call:
```python
result = perplexity_search("What are the latest AI trends in 2025?")
```

### Response Object:
```json
{
  "success": true,
  "content": "The latest AI trends in 2025 include the rapid advancement of agentic AI, greater model specialization, enterprise-scale adoption, major scientific breakthroughs, and increasing accessibility and efficiency of models.",
  "citations": [
    "https://example.com/ai-trends-2025",
    "https://example.com/agentic-ai",
    "https://example.com/model-specialization"
  ],
  "search_type": "pro",
  "markdown": "# Search Results\n\n**Query:** What are the latest AI trends in 2025?\n\n**Search Type:** pro\n\n## Answer\n\nThe latest AI trends in 2025 include the rapid advancement of agentic AI, greater model specialization, enterprise-scale adoption, major scientific breakthroughs, and increasing accessibility and efficiency of models.\n\n## Sources\n\n1. https://example.com/ai-trends-2025\n2. https://example.com/agentic-ai\n3. https://example.com/model-specialization"
}
```

### Markdown Preview:
```markdown
# Search Results

**Query:** What are the latest AI trends in 2025?

**Search Type:** pro

## Answer

The latest AI trends in 2025 include the rapid advancement of agentic AI,
greater model specialization, enterprise-scale adoption, major scientific
breakthroughs, and increasing accessibility and efficiency of models.

## Sources

1. https://example.com/ai-trends-2025
2. https://example.com/agentic-ai
3. https://example.com/model-specialization
```

---

## Example 2: Social Search Response

### Call:
```python
result = perplexity_social(
    "What are developers discussing about AI safety?",
    save_to_file="ai_safety_discussion.md"
)
```

### Response Object:
```json
{
  "success": true,
  "content": "Developers are actively discussing increasing pressures around AI safety, calling for robust safeguards, regulatory frameworks, and greater transparency to prevent harmful or catastrophic risks from advanced AI systems.",
  "citations": [
    "https://x.com/thread/ai-safety-discussion",
    "https://reddit.com/r/MachineLearning/ai-safety",
    "https://github.com/discussions/ai-safety"
  ],
  "search_focus": "social",
  "markdown": "# Search Results\n\n**Query:** What are developers discussing about AI safety?\n\n**Search Focus:** social\n**Search Type:** pro\n\n## Answer\n\nDevelopers are actively discussing increasing pressures around AI safety, calling for robust safeguards, regulatory frameworks, and greater transparency to prevent harmful or catastrophic risks from advanced AI systems.\n\n## Sources\n\n1. https://x.com/thread/ai-safety-discussion\n2. https://reddit.com/r/MachineLearning/ai-safety\n3. https://github.com/discussions/ai-safety",
  "file_saved": "/Users/markus/perplexity/ai_safety_discussion.md"
}
```

### File Saved As `ai_safety_discussion.md`:
```markdown
# Search Results

**Query:** What are developers discussing about AI safety?

**Search Focus:** social
**Search Type:** pro

## Answer

Developers are actively discussing increasing pressures around AI safety,
calling for robust safeguards, regulatory frameworks, and greater transparency
to prevent harmful or catastrophic risks from advanced AI systems.

## Sources

1. https://x.com/thread/ai-safety-discussion
2. https://reddit.com/r/MachineLearning/ai-safety
3. https://github.com/discussions/ai-safety
```

---

## Example 3: Using in Claude Code

### You Ask:
```
Search for the latest quantum computing breakthroughs using perplexity_search
and save the results to quantum_research.md
```

### Claude Code Calls:
```python
perplexity_search(
    query="latest quantum computing breakthroughs",
    search_type="pro",
    save_to_file="quantum_research.md"
)
```

### Claude Code Receives:
```json
{
  "success": true,
  "content": "Recent quantum computing breakthroughs in 2025 include...",
  "citations": [...],
  "search_type": "pro",
  "markdown": "# Search Results\n...",
  "file_saved": "quantum_research.md"
}
```

### Claude Code Shows You:
```
✓ Search completed successfully

📄 Quantum Computing Breakthroughs

Recent quantum computing breakthroughs in 2025 include...

[Full formatted results]

💾 Saved to: quantum_research.md
```

---

## Example 4: Error Response

### Call:
```python
result = perplexity_search("query here", save_to_file="/invalid/path.md")
```

### Response on Error:
```json
{
  "success": false,
  "error": "Permission denied when accessing /invalid/path",
  "content": null,
  "citations": [],
  "file_error": "Permission denied: /invalid/path.md"
}
```

### Or API Error:
```json
{
  "success": false,
  "error": "Rate limit exceeded. Please wait 60 seconds before next request.",
  "content": null,
  "citations": []
}
```

---

## Example 5: Different Search Types

### Fast Search:
```python
result = perplexity_search(
    "Quick AI summary",
    search_type="fast"
)
# Returns quicker, less comprehensive results
# Lower API cost
```

### Auto Search:
```python
result = perplexity_search(
    "Complex research topic",
    search_type="auto"
)
# Perplexity decides search depth
# Balanced speed and accuracy
```

### Pro Search (default):
```python
result = perplexity_search(
    "Deep research needed",
    search_type="pro"
)
# Deep web crawling
# Most comprehensive
# Higher API cost
```

---

## Example 6: Accessing Different Parts

### Just the Answer:
```python
result = perplexity_search("question")
print(result['content'])
# Output: Plain text answer only
```

### Just the Markdown:
```python
result = perplexity_search("question")
print(result['markdown'])
# Output: Full formatted markdown for sharing/saving
```

### Just the Sources:
```python
result = perplexity_search("question")
for source in result['citations']:
    print(f"- {source}")
# Output:
# - https://source1.com
# - https://source2.com
# - https://source3.com
```

### Check Success First:
```python
result = perplexity_search("question")
if result['success']:
    # Use result['content'], result['citations'], result['markdown']
    pass
else:
    print(f"Error: {result['error']}")
```

---

## Output Summary Table

| Scenario | Use This | Example |
|----------|----------|---------|
| Quick processing | `result['content']` | Summarize for email |
| Share with others | `result['markdown']` | Post to knowledge base |
| Save for later | `save_to_file` param | Archive research |
| Check sources | `result['citations']` | Create bibliography |
| Debug issues | `result['success']`, `result['error']` | Error handling |
| Check metadata | `result['search_type']` | Track API usage |

---

## File Output Examples

When using `save_to_file="research.md"`, the file will contain:

**File: research.md**
```markdown
# Search Results

**Query:** Your search query here

**Search Type:** pro

## Answer

[Full detailed answer with multiple paragraphs,
bullet points, and formatted text as provided
by Perplexity AI]

## Sources

1. https://source1.com
2. https://source2.com
3. https://source3.com
```

The file is ready to:
- View in any markdown reader
- Commit to version control
- Share with team members
- Include in documentation
- Post on wikis or blogs
