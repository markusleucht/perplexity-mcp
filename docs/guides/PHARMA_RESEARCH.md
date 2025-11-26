# Pharma-Research Skill Guide

**Last Updated:** November 26, 2025
**Version:** v2.1.0 (Production-Ready)
**Audience:** German pharmaceutical sales & marketing teams
**Output Language:** German (Deutsch)
**Prerequisites:** Claude Code, Perplexity MCP server

---

## What It Does

Automatically conducts structured business analysis of German pharma markets **IN GERMAN** for sales & marketing teams:

### Core Analysis (all reports):
- **Indikationsanalyse:** Epidemiologie, Versorgungslücken, Behandlungspfade
- **Medikamentenanalyse:** Wettbewerb, Differenzierung, Marktzugang, Barrieren
- **SWOT-Analyse:** Strategische Stärken, Schwächen, Chancen, Risiken **(NEW in v2.1.0)**
- **Geschäftsempfehlungen:** Zielpopulationen, Positionierung, Key Messages **(NEW in v2.1.0)**

### Sales-Focused Content (v2.1.0):
- **Facharztlandschaft:** Anzahl, Spezialisierung, Verschreibungsverhalten
- **Verschreibungsbarrieren:** Regressangst, Bürokratie, konservative Einstellung
- **Regionale Disparitäten:** Wo sind die größten Versorgungslücken?
- **Wettbewerbsargumente:** Head-to-Head-Daten für Ärztegespräche
- **Einwandbehandlung:** Wie reagiert man auf Sicherheitsbedenken?

### Quality:
- **Sprache:** Deutsch (alle Berichte)
- **Quellen:** 20-30 autoritäre Quellen (RKI, G-BA, KBV, Fachgesellschaften)
- **Zahlen:** Alle Statistiken mit Jahreszahl
- **Validated:** Erfolgreich getestet mit Psoriasis/Bimekizumab-Analyse

---

## Usage

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

---

## Real-World Example

**Query:** "Analysiere den deutschen Pharmamarkt für Psoriasis und Bimzelx"

**Result (v2.1.0) - German Output:**
- 5-7 Seiten strategischer Geschäftsbericht **auf Deutsch**
- **Epidemiologie:** 2,2 Mio. Patienten, 2-3% Prävalenz, 420.000 mittelschwer bis schwer
- **Versorgungslücke:** 73% ohne Biologika = 308.000 Unterversorgte
- **Facharztlandschaft:** 6.511 Dermatologen, nur 254 Psoriasis-Spezialisten (4%)
- **Verschreibungsbarrieren:** Regressangst, Bürokratie, 8-facher Unterschied zwischen Bundesländern
- **SWOT-Analyse:** Stärken (überlegene PASI-Raten), Schwächen (Candida-Risiko), Chancen (Non-Responder), Risiken (IL-23-Konkurrenz)
- **Zielpopulationen:** Non-Responder auf IL-17A, PASI-100-Sucher, Unterversorgte
- **Positionierung:** "Bimzelx – Für Patienten, die mehr erwarten"
- **Key Message für Außendienst:** Überlegene Hautklarheit, dualer Mechanismus
- 25-30 Quellen (RKI, G-BA, KBV, Psoriasis-Netz, PMC)
- Kosten: ~$0.08 (8 Recherchen @ "auto" Modus)

---

## Installation

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

---

## Documentation

- **Skill README:** `~/.claude/skills/pharma-research/README.md` (complete setup & usage guide)
- **Skill Definition:** `~/.claude/skills/pharma-research/SKILL.md` (research framework)
- **Query Strategies:** `~/.claude/skills/pharma-research/references/query-strategies.md`
- **Example Report:** `~/.claude/skills/pharma-research/examples/Psoriasis_Bimzelx_UCB_Example.md` **(NEW in v2.0.0)**
- **GitHub Repository:** https://github.com/markusleucht/claude-code-skills

---

## Cost per Report

- **Typical analysis with company context:** 6-10 Perplexity searches @ "auto" mode
- **Cost:** ~$0.06-0.10 per comprehensive report (was $0.03-0.045 in v1.0.0)
- **Cost breakdown:**
  - Indication analysis: 2-3 searches (~$0.02)
  - Company/portfolio analysis: 3-4 searches (~$0.03-0.04) **[NEW]**
  - Medication analysis: 2-3 searches (~$0.02)
- **Your $5 budget:** ~50-80 detailed pharma market reports with portfolio context

---

## Related Documentation

- **Skill Manifest** → [`../tools/skills.md`](../tools/skills.md)
- **MCP Server Tools** → [`../tools/mcp-servers.md`](../tools/mcp-servers.md)
- **User Guide** → [`USER_GUIDE.md`](USER_GUIDE.md)
- **Developer Guide** → [`DEVELOPER_GUIDE.md`](DEVELOPER_GUIDE.md)
- **GitHub Repository** → https://github.com/markusleucht/claude-code-skills
