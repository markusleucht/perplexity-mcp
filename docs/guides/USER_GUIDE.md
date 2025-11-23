# Perplexity MCP User Guide

**Last Updated:** November 23, 2025
**Audience:** End users of Perplexity MCP with Claude Code
**Prerequisites:** Perplexity MCP server installed and configured

---

## What You Get Back

### Markdown Report
```
[Content section with analysis]

## Quellen

1. https://example.com/source1
2. https://example.com/source2
...

---

*Recherchiert: 22. November 2025*
*Methode: Perplexity Pro Search auf Web-Quellen (sonar-pro)*
*Anfrage: Your query here*
```

### Features
- ✅ Professional report format
- ✅ Actual source URLs (not hallucinated)
- ✅ Current date included
- ✅ Method metadata
- ✅ Ready to share/publish

---

## Real-World Queries

### Research Papers
```
Search for recent breakthroughs in quantum computing using scholar sources
```

### Industry Trends
```
Find the top emerging trends in healthcare technology for 2025
```

### News & Discussion
```
What are people discussing about cryptocurrency regulations?
```

### Competitive Analysis
```
Search for what competitors are doing with AI implementation
```

### Market Research
```
Find consumer trends in sustainable fashion for 2025
```

---

## Understanding the Output

### Citation Numbers
Content includes numbers like `[1][2][3]` - these correspond to the sources list below.

### Sources Section
All sources are **real URLs** extracted from Perplexity's search results. They are NOT hallucinated by the AI.

### Metadata Footer
- **Recherchiert:** Date the search was performed
- **Methode:** Which Perplexity model and source type was used
- **Anfrage:** The exact query that was searched

---

## Tips & Tricks

### Get Better Results
- Be specific about what you want
- Include year/timeframe if relevant ("2025", "recent")
- Mention the audience/context

### Handling Large Topics
- Use `search_type="pro"` for deep research (default)
- Use `search_type="auto"` for balanced search
- Use `search_type="fast"` for quick results

### Language Support
The tool auto-detects language, but you can be explicit:
- German: "auf Deutsch"
- Spanish: "en español"
- French: "en français"

### Save for Later
Always use `save_to_file` parameter to keep reports:
```
Search for "topic" and save as "my_report.md"
```

---

## Integration Examples

### Example 1: Quick Market Research
```
User: "Search for upcoming AI regulations in Europe for 2025"
Claude Code: Performs search, returns 15-page report with 20 sources
User: Reads report, gets sources, makes decisions
```

### Example 2: Competitive Intelligence
```
User: "Find what major tech companies are saying about AI safety"
Claude Code: Searches social media, returns discussion summary with sources
```

### Example 3: Documentation
```
User: "Research Python async programming best practices and save as guide.md"
Claude Code: Creates guide.md with professional report format
```

---

## Related Documentation

- **Quick Start** → [`QUICKSTART.md`](QUICKSTART.md)
- **Developer Reference** → [`DEVELOPER_GUIDE.md`](DEVELOPER_GUIDE.md)
- **Troubleshooting** → [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
- **Pharma Research** → [`PHARMA_RESEARCH.md`](PHARMA_RESEARCH.md)
- **MCP Server Tools** → [`../tools/mcp-servers.md`](../tools/mcp-servers.md)
