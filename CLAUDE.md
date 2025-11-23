# Using Perplexity MCP with Claude Code

**Quick reference for integrating Perplexity searches directly into Claude Code.**

---

## What This Tool Does

With this MCP server, you can ask Claude Code to:
- Search Perplexity AI Pro Search (deep research with web crawling)
- Search social media and expert forums
- Get German-language reports
- Save results as markdown files
- **NEW:** Built-in research guidelines for precise, data-driven answers
- **NEW:** Automated German pharmaceutical market research via `pharma-research` skill

Everything happens through natural language - just ask!

### Research Quality Guidelines

Every search is automatically guided by these principles:
- **Specific data with years** (no generic statements)
- **Context**: changes over time + benchmarks
- **Transparent**: clearly states when data is unavailable
- **Structured**: Key facts → Data points → Interpretation → Sources

---

## Quick Start

### 1. First-Time Setup (One Command)

If this is your first time using the tool, run:

```bash
chmod +x setup.sh && ./setup.sh
```

This automatically installs dependencies and configures everything. Then restart Claude Code.

**Already set up?** Skip to step 2.

### 2. Basic Searches in Claude Code

```
Search for "quantum computing trends in 2025"
```

Claude Code will call the tool and return a markdown report with sources.

---

## Natural Language Examples

### Pro Search (Deep Research)
```
Search for the latest AI developments in 2025
```
→ Performs deep research with web crawling, returns comprehensive report with 15-20 sources

### Social Media Focus
```
Search social media for what people are discussing about AI safety
```
→ Searches Twitter, Reddit, forums, expert discussions

### German Language
```
Search für Entwicklungen in der Medizin 2025
```
→ Returns German-language report (query language detected)

### Save to File
```
Search for machine learning trends and save to trends.md
```
→ Creates `reports/trends.md` with complete report (automatically saved to `reports/` folder)

### Language Selection
```
Search for renewable energy trends in Spanish
```
→ Returns Spanish-language response

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

## Tool Parameters (If You Need Control)

If you want to be explicit about parameters:

| Parameter | Values | Default | Example |
|-----------|--------|---------|---------|
| `query` | Any text | Required | "AI trends 2025" |
| `search_type` | pro, auto, fast | pro | "fast" |
| `sources` | web, social, scholar | web | "social" |
| `language` | en, de, es, fr, it | en | "de" |
| `max_tokens` | 100-4000 | 1024 | 2000 |
| `save_to_file` | Path/filename | None | "report.md" |

### Example with Parameters
```
Pro Search: "What are the latest cancer treatments?"
German language, save as "Krebsbehandlung_2025.md"
```

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

## File Locations

```
/Users/markus/perplexity/
├── .env                    # Your API key (never commit)
├── .mcp.json              # MCP server config (already set up)
├── README.md              # Project overview
├── src/
│   └── perplexity_mcp.py  # The actual tool code
├── docs/
│   ├── QUICKSTART.md
│   ├── SESSION_SUMMARY.md # Latest changes
│   └── ... (other docs)
└── reports/               # All generated reports (auto-created)
    ├── Dermatologen_Deutschland_2025.md
    ├── Psoriasis_Therapien_2025.md
    └── ... (your search results)
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

## API Costs

- **Pro Search:** ~$0.01-0.02 per query
- **Social Search:** ~$0.01-0.02 per query
- **Your Budget:** $5 in credits
- **Expected Usage:** 100-250 searches before credits depleted

Monitor at: https://www.perplexity.ai/settings/api

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

## Troubleshooting

### "API key not found"
Check that `.env` file exists with `PERPLEXITY_API_KEY=pplx-...`

### No results returned
- Try different search query
- Check API credits: https://www.perplexity.ai/settings/api
- Try `search_type="auto"` instead of "pro"

### Not getting sources
Sources come from Perplexity's search results. If none appear, the search may not have found relevant sources.

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

## Next Steps

1. **Try a simple search** in Claude Code
2. **Review the generated report** in the IDE
3. **Check the sources** - they're all real and verifiable
4. **Customize for your needs** - change language, source type, etc.

---

## For Developers

The MCP tools are defined in `src/perplexity_mcp.py`:

```python
def perplexity_search(
    query: str,
    search_type: str = "pro",
    max_tokens: int = 1024,
    sources: list = None,
    language: str = "en",
    save_to_file: str = None,
) -> Dict[str, Any]

def perplexity_social(
    query: str,
    max_tokens: int = 1024,
    save_to_file: str = None,
) -> Dict[str, Any]
```

Both return:
```python
{
    "success": True/False,
    "content": "Text answer",
    "markdown": "Formatted report",
    "citations": ["url1", "url2", ...],
    "file_saved": "path/to/file.md",  # if requested
    "error": "Error message"  # if failed
}
```

---

## Pharma-Research Skill (Production-Ready - v2.0.0)

For German pharmaceutical market research with company portfolio context, a specialized Claude Code skill is available:

### What It Does

Automatically conducts structured business analysis of German pharma markets with strategic portfolio context:
- **Indication Analysis:** Epidemiology, unmet needs, care pathways, market access
- **Medication Analysis:** Competition, differentiation, pricing, adoption barriers, opportunities
- **Company Portfolio Analysis:** Corporate financials, portfolio composition, strategic product positioning **(NEW in v2.0.0)**
- **Marketing Investment Scoring:** 1-5 star priority rating with budget recommendations **(NEW in v2.0.0)**
- **Negotiation Context:** Leverage assessment, partnership potential, budget tier guidance **(NEW in v2.0.0)**
- **Quality:** Data-driven reports with 20-30 sources, specific numbers with years
- **Production-Validated:** Successfully tested with real-world analysis (Psoriasis, Bimekizumab & UCB Pharma)

### Usage

Just ask naturally:
```
"Analyze the German pharmaceutical market for Psoriasis and Bimekizumab"
"Analyze Psoriasis, Bimekizumab, and UCB Pharma's portfolio position"
"What role does Ozempic play in Novo Nordisk's portfolio strategy?"
"Research Diabetes Type 2 and Ozempic in Germany"
```

The skill automatically:
1. Extracts indication, medication, and company parameters (auto-detects if not specified)
2. Performs 6-10 targeted Perplexity searches (German + English)
   - Phase 1: Indication epidemiology
   - Phase 2: Company financials and portfolio
   - Phase 3: Medication market position
   - Phase 4: Strategic positioning and peak sales
3. Calculates marketing investment priority score (1-5 stars)
4. Synthesizes findings into structured business report with budget recommendations
5. Delivers 5-7 page report with 20-30 sources
6. Saves report to `reports/` folder

### Real-World Example

**Query:** "Analyze the German pharmaceutical market for Psoriasis, Bimekizumab, and UCB Pharma"

**Result (v2.0.0):**
- 5-7 page comprehensive business report with 3 major sections
- **Indication:** 2.2M patients, 2-3% prevalence, biologics adoption 35%
- **Medication:** Dual IL-17A/F inhibitor, PASI 90: 84-93%, market share 5-8%
- **Company:** UCB 6.15 Mrd. EUR revenue, 29% R&D ratio, portfolio transformation
- **Portfolio Position:** Bimzelx 799 Mio. EUR (H1 2025), peak sales >4 Mrd. EUR target, 26% revenue share
- **Strategic Role:** Growth Driver compensating Cimzia patent loss, mission-critical
- **Investment Priority:** ⭐⭐⭐⭐⭐ (5/5) - Blockbuster launch
- **Budget Recommendation:** Premium tier, high negotiation leverage, long-term partnership potential
- 25-30 authoritative sources (RKI, G-BA, UCB investor reports, Fierce Pharma)
- Cost: ~$0.08 (8 searches @ "auto" mode)

### Installation

**Already installed** in your user-level skills directory (`~/.claude/skills/pharma-research/`).

**To use on another machine:**
```bash
git clone https://github.com/markusleucht/claude-code-skills.git
cp -r claude-code-skills/pharma-research ~/.claude/skills/
# Restart Claude Code
```

**Requirements:**
- Claude Code
- Perplexity MCP server configured (this project)

### Documentation

- **Skill README:** `~/.claude/skills/pharma-research/README.md` (complete setup & usage guide)
- **Skill Definition:** `~/.claude/skills/pharma-research/SKILL.md` (research framework)
- **Query Strategies:** `~/.claude/skills/pharma-research/references/query-strategies.md`
- **Example Report:** `~/.claude/skills/pharma-research/examples/Psoriasis_Bimzelx_UCB_Example.md` **(NEW in v2.0.0)**
- **GitHub Repository:** https://github.com/markusleucht/claude-code-skills

### Cost per Report

- **Typical analysis with company context:** 6-10 Perplexity searches @ "auto" mode
- **Cost:** ~$0.06-0.10 per comprehensive report (was $0.03-0.045 in v1.0.0)
- **Cost breakdown:**
  - Indication analysis: 2-3 searches (~$0.02)
  - Company/portfolio analysis: 3-4 searches (~$0.03-0.04) **[NEW]**
  - Medication analysis: 2-3 searches (~$0.02)
- **Your $5 budget:** ~50-80 detailed pharma market reports with portfolio context

---

## Resources

### Perplexity MCP Documentation
- **Quick Start:** `docs/QUICKSTART.md`
- **All Changes:** `docs/SESSION_SUMMARY.md`
- **Output Details:** `docs/OUTPUT_FORMAT.md`
- **Examples:** `docs/OUTPUT_EXAMPLES.md`
- **Setup Notes:** `docs/SETUP_COMPLETE.md`

### Skill Documentation
- **Implementation Plan:** `docs/plan.md`
- **Setup Complete:** `docs/SKILL_SETUP_COMPLETE.md`
- **GitHub Portability:** `docs/GITHUB_PORTABILITY.md`

### Changelog
- **All Changes:** `CHANGELOG.md`

---

**Ready to search? Just ask Claude Code!** 🚀
