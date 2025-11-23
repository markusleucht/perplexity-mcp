# Output Templates & Quality Guidelines

This document contains templates, checklists, and detailed formatting guidance for pharma-research skill outputs.

## Output Structure Template

Deliver findings in this exact format:

### [Indication Name] – [Medication Name] | German Market Analysis

#### 1) Indication: [Name] (Germany)

**Epidemiology & Market Size**
- [5-8 bullet points with specific numbers and years]

**Unmet Need**
- [3-5 bullet points quantifying treatment gaps]

**Care Pathway & Access**
- [4-6 bullet points on specialists, guidelines, reimbursement]

**Key Insights:**
[5-8 concise bullet points synthesizing the most important findings with numbers]

**Interpretation:**
[3-5 sentences providing business context and implications]

#### 2) Medication: [Name] (Germany)

**Market Position & Competition**
- [4-6 bullet points on competitive landscape]

**Differentiation**
- [3-5 bullet points on unique value proposition]

**Market Access**
- [4-5 bullet points on pricing, AMNOG, reimbursement]

**Adoption Barriers**
- [3-5 bullet points on challenges]

**Risks & Opportunities**
- [4-6 bullet points on future outlook]

**Key Insights:**
[5-8 concise bullet points synthesizing medication-specific findings]

**Interpretation:**
[3-5 sentences on strategic implications and positioning]

#### Data Points
- [Bulleted list of all specific statistics with year]
- [Include: numbers, percentages, growth rates, comparisons]

#### Quellen
1. [Institution/Source Name] ([Year]) - [URL]
2. [Institution/Source Name] ([Year]) - [URL]
[Continue numbering all sources]

---

*Recherchiert: [Date]*
*Methode: Perplexity Pro Search auf Web-Quellen (sonar-pro)*
*Anfrage: [Original user query]*

## Quality Checklist

Before finalizing the report, verify:

- [ ] All numbers include year/date
- [ ] Change over time shown for key metrics
- [ ] Benchmark comparisons included where relevant
- [ ] Data gaps explicitly stated (no speculation)
- [ ] Sources are authoritative (official stats, professional associations)
- [ ] German terminology used consistently
- [ ] Business implications clearly articulated
- [ ] Report saved to file if requested

## Data Validation Standards

**Requirements:**
- **Specific data with years** - Never use generic claims without numbers and dates
- **Context** - Always show change over time + relevant benchmarks
- **Transparency** - Clearly state when reliable data is unavailable (no guessing)
- **Structured** - Follow format: Key facts → Data points → Interpretation → Sources

**Data source hierarchy (prioritize in this order):**
1. Official statistics: Destatis, RKI, KBV, Kassenärztliche Vereinigung
2. Professional associations: DGHO, DDG, DGK, specialty societies
3. Health insurance data: AOK, Barmer, TK reports
4. Industry reports: IQVIA, Insight Health (verify recency)
5. Academic studies: peer-reviewed publications
6. Media reports: Use only for context, not primary data

**Red flags (verify carefully):**
- Outdated data (>3 years old without noting limitations)
- Conflicting numbers across sources (investigate discrepancy)
- Industry-sponsored data without independent validation
- Vague terms ("many", "most", "growing") without quantification

## Tips for Effective Research

**Maximize Perplexity search quality:**
- Use precise German medical/pharma terminology
- Include year in queries for recent data
- Combine general terms + specific drug/disease names
- Search incrementally: broad → specific → validation

**Handle data gaps:**
- State explicitly: "Keine aktuellen Daten verfügbar für [metric]"
- Provide related available data as proxy if reasonable
- Note data limitations in interpretation section

**Optimize for business utility:**
- Lead with actionable insights (market size, growth, competitive threats)
- Quantify unmet needs in patient numbers or economic terms
- Highlight differentiation factors that affect market access
- Connect epidemiology to commercial opportunity

## Example Application

**User query:** "Analyze the German pharmaceutical market for Psoriasis and Cosentyx"

**Skill execution:**
1. Extract parameters: Indication = Psoriasis, Medication = Cosentyx
2. Formulate 5-6 German Perplexity queries covering all framework dimensions
3. Execute searches with `language="de"`, `search_type="auto"`
4. Synthesize findings following output structure
5. Validate data quality (years, sources, context)
6. Generate markdown report with sources
7. Save to `reports/Psoriasis_Cosentyx_[date].md`

**Expected output:** 3-5 page business-oriented report with 15-25 cited sources, specific numbers with years, clear competitive positioning, and actionable market insights.
