# Plan: Erweiterung pharma-research Skill um Firmenanalyse

**Ziel:** pharma-research um dritten Parameter "Firma" erweitern, um die strategische Position des Medikaments im Portfolio des Herstellers zu verstehen.

**Datum:** 23. November 2025

---

## 1. Überblick

### Aktuelle Parameter
- **Indikation** (z.B. Psoriasis)
- **Medikament** (z.B. Bimekizumab)

### Neuer Parameter
- **Firma** (z.B. UCB Pharma)

### Anwendungsfall
Als Analyst für digitales Pharmamarketing verstehen, welche Rolle ein Medikament im Portfolio der Pharmafirma spielt, wenn diese mit einer Kampagne auf euch zukommt.

---

## 2. Analyse-Framework: Firma & Portfolio

### 2.1 Firmen-Grunddaten

**Unternehmensstruktur:**
- Firmenname, Hauptsitz, Gründungsjahr
- Konzernzugehörigkeit (eigenständig vs. Teil eines Konzerns)
- Börsennotierung, Eigentümerstruktur
- Mitarbeiteranzahl

**Finanzdaten:**
- Gesamtumsatz (aktuellstes Jahr mit Quelle)
- Umsatzentwicklung (3-5 Jahre Trend)
- F&E-Quote (% des Umsatzes)
- EBITDA-Marge
- Geografische Umsatzverteilung (wenn verfügbar)

**Strategische Ausrichtung:**
- Therapiegebiete / Fokus-Bereiche
- Hauptmärkte (geografisch)
- Unternehmensstrategie (aus Geschäftsberichten)

### 2.2 Portfolio-Analyse

**Bestand-Portfolio:**
- Liste der 5-10 wichtigsten Medikamente
- Jeweiliger Umsatz (wenn verfügbar)
- Lifecycle-Stage (Launch, Growth, Mature, Decline)
- Patentabläufe (kritisch für Umsatzplanung)

**Pipeline:**
- Medikamente in Phase 3 (kurz vor Markteintritt)
- Medikamente in Phase 2 (mittelfristig)
- Fokus-Indikationen in Entwicklung

**Portfolio-Dynamik:**
- Welche Produkte verlieren Patentschutz?
- Welche neuen Launches kompensieren Verluste?
- Gibt es Portfolio-Transformationen?

### 2.3 Medikament im Portfolio-Kontext

**Quantitative Position:**
- Umsatz des Medikaments (aktuell)
- Umsatzentwicklung (3-5 Jahre)
- Anteil am Gesamtumsatz (%)
- Peak Sales Guidance (Unternehmensprognose)
- Wachstumsrate vs. Portfolio-Durchschnitt

**Qualitative Bedeutung:**
- **Strategische Rolle:**
  - Blockbuster / Growth Driver / Maintenance Product
  - Kompensiert das Medikament Patentverluste?
  - Teil einer Indikations-Familie oder Stand-alone?
- **Lifecycle-Bewertung:**
  - Launch (0-3 Jahre): Aggressive Investition
  - Growth (3-8 Jahre): Marktanteilsgewinn
  - Mature (8-15 Jahre): Cash Cow
  - Decline (>15 Jahre / Post-Patent): Auslauf
- **Portfolio-Fit:**
  - Passt zu bestehenden Therapiegebieten?
  - Erweitert Portfoliobreite (neue Indikation)?
  - Ersetzt älteres Produkt?

**Wettbewerbskontext:**
- Hauptkonkurrenten (Produkte anderer Firmen)
- Marktposition (Marktführer, Challenger, Nischenprodukt)
- Differenzierung (Alleinstellungsmerkmale)

### 2.4 Marketing-Implikationen

**Investment-Bereitschaft (Scoring):**
- **5/5 Sterne:** Blockbuster-Launch, >30% geplanter Umsatzanteil
- **4/5 Sterne:** Wichtiges Wachstumsprodukt, 15-30% Umsatzanteil
- **3/5 Sterne:** Solides Portfolio-Element, 5-15% Umsatzanteil
- **2/5 Sterne:** Maintenance-Produkt, <5% Umsatzanteil
- **1/5 Sterne:** Auslaufprodukt, Post-Patent

**Budget-Indikation:**
- Launch-Phase: Hohe Marketingbudgets erwartet
- Growth-Phase: Moderate bis hohe Budgets
- Mature-Phase: Selektive Investments
- Decline-Phase: Minimale Marketingausgaben

**Verhandlungsposition:**
- Hohe Priorität → Firma wird investieren wollen
- Patentablauf droht → Zeitdruck, mögliche Rabatte
- Nischenprodukt → Budget begrenzt, Effizienz wichtig

---

## 3. Research-Methodik: Perplexity Queries

### 3.1 Firmen-Recherche (3-4 Queries)

**Query 1: Firmenbasis**
```
[Firma] Pharma Konzernstruktur Umsatz Geschäftsbericht [Jahr]
```
*Ziel:* Grunddaten, Konzernzugehörigkeit, Finanzkennzahlen

**Query 2: Portfolio-Übersicht**
```
[Firma] wichtigste Medikamente Portfolio Therapiegebiete
```
*Ziel:* Hauptprodukte, strategische Schwerpunkte

**Query 3: Pipeline & Strategie**
```
[Firma] Pipeline Entwicklung Phase 3 Patentablauf
```
*Ziel:* Zukünftige Produkte, ablaufende Patente

**Query 4: Firmenhistorie & Fokus (optional)**
```
[Firma] Übernahmen Fusionen strategische Neuausrichtung [letzte 5 Jahre]
```
*Ziel:* Kontext für Portfolio-Transformationen

### 3.2 Medikament-im-Portfolio (2-3 Queries)

**Query 5: Produktumsatz**
```
[Medikament] [Firma] Umsatz revenue sales [Jahr]
```
*Ziel:* Konkrete Umsatzzahlen, Entwicklung

**Query 6: Strategische Bedeutung**
```
[Firma] [Medikament] Peak Sales Blockbuster Wachstumsstrategie
```
*Ziel:* Unternehmensprognosen, Positionierung

**Query 7: Portfolio-Kontext (optional)**
```
[Firma] Patentablauf [Jahr] [Medikament] Ersatzprodukt
```
*Ziel:* Versteht, ob Medikament Lücken füllt

### Sprache & Parameter
- **Queries auf Deutsch**, wenn deutsche Geschäftsberichte relevant
- **Queries auf Englisch**, für internationale Daten (Börsenmeldungen, SEC filings)
- **search_type: "auto"** (Standard, ausgewogen)
- **max_tokens: 1500-2000** (mehr Kontext für Finanzanalysen)

---

## 4. Output-Struktur (Ergänzung zu bestehendem Report)

### Neue Sektion im Markdown-Report

```markdown
#### 3) Firma: [Firmenname] – Portfolio-Kontext

**Unternehmensübersicht**
- Konzernstruktur: [Eigenständig / Teil von X]
- Gesamtumsatz [Jahr]: [X Mrd. EUR/USD]
- F&E-Quote: [X% des Umsatzes]
- Mitarbeiter: [Anzahl]
- Fokus-Bereiche: [Therapiegebiete]
- Hauptmärkte: [USA, Europa, etc.]

**Portfolio-Übersicht**
- Top-Produkte (nach Umsatz):
  1. [Produkt 1]: [X Mio. EUR] – [Indikation]
  2. [Produkt 2]: [X Mio. EUR] – [Indikation]
  3. ...
- Pipeline-Schwerpunkte: [Phase 3 Produkte]
- Kritische Patentabläufe: [Produkt, Jahr]

**Position von [Medikament] im Portfolio**

*Quantitative Einordnung:*
- Produktumsatz [Jahr]: [X Mio. EUR]
- Umsatzanteil: [X%] des Gesamtumsatzes
- Wachstumsrate: [+X%] YoY
- Peak Sales Guidance: [X Mrd. EUR/USD] (Quelle: [X])

*Strategische Rolle:*
- Lifecycle-Stage: [Launch / Growth / Mature / Decline]
- Portfolio-Funktion: [Growth Driver / Blockbuster / Cash Cow / Nische]
- Strategische Bedeutung:
  - [Bullet: z.B. "Kompensiert Patentverlust von Produkt X"]
  - [Bullet: z.B. "Teil der Expansion in Therapiegebiet Y"]
  - [Bullet: z.B. "Wichtigster Launch der letzten 5 Jahre"]

*Wettbewerbsposition:*
- Hauptkonkurrenten: [Produkt 1 (Firma A), Produkt 2 (Firma B)]
- Marktposition: [Marktführer / Challenger / Aufsteiger / Nische]
- Differenzierung: [Alleinstellungsmerkmal]

**Key Insights: Portfolio-Implikationen**
- [5-8 Bullet Points mit konkreten Zahlen]
- Beispiele:
  - "Bimzelx soll bei Peak Sales 40-50% des UCB-Umsatzes ausmachen"
  - "Kompensiert Umsatzeinbußen durch Cimzia-Patentverlust (2024)"
  - "UCB investiert 29% des Umsatzes in F&E, überdurchschnittlich hoch"

**Interpretation: Marketing-Bereitschaft**

*Investment-Priorität:* ⭐⭐⭐⭐⭐ (5/5)

[3-5 Sätze Business-Kontext:]
- "Als [Rolle im Portfolio] mit [Peak Sales Erwartung] ist dieses Medikament
  von höchster strategischer Bedeutung für [Firma]."
- "Die Firma befindet sich in [Lifecycle/Transformation], was [Implikation
  für Marketingbudgets]."
- "Erwartung: [Hohe/Moderate/Geringe] Investitionsbereitschaft in digitale
  Kanäle."

*Empfehlung für Kampagnen-Budgetverhandlung:*
- [Konkrete Handlungsempfehlung basierend auf Portfolio-Position]
- Beispiel: "Als Launch-Produkt mit Blockbuster-Potential erwarten Sie
  aggressive Kampagnenbudgets. Positionieren Sie Premium-Pakete
  (Microsites + Newsletter + Kongress-Banner)."
```

---

## 5. Implementierung: Code-Änderungen

### 5.1 SKILL.md Anpassungen

**In `~/.claude/skills/pharma-research/SKILL.md`:**

1. **Description erweitern** (Zeile 3):
```markdown
description: Precision research assistant for analyzing the German pharmaceutical
market with company portfolio context. Use when users need business-oriented
assessment of specific indications, medications, AND the pharmaceutical company's
portfolio strategy in Germany...
```

2. **Neue Sektion einfügen** nach "Part 2: Medication Analysis":
```markdown
### Part 3: Company & Portfolio Analysis

**1. Company Overview**
- Corporate structure, ownership, financials
- Therapeutic focus areas and geographic markets
- R&D investment (% of revenue)

**2. Portfolio Position**
- Top products by revenue
- Pipeline (Phase 3/4 products)
- Patent expirations threatening revenue

**3. Strategic Role of Medication**
- Quantitative: Revenue, growth rate, % of total
- Qualitative: Lifecycle stage, portfolio function
- Competitive context within company portfolio

**4. Marketing Implications**
- Investment priority scoring (1-5 stars)
- Budget expectations based on lifecycle
- Negotiation positioning
```

3. **Query-Beispiele ergänzen** (Zeile 88-107):
```markdown
**Company/Portfolio queries:**
- "[Firma] Pharma Konzernstruktur Umsatz [Jahr]"
- "[Firma] wichtigste Medikamente Portfolio"
- "[Medikament] [Firma] Umsatz revenue Peak Sales"
- "[Firma] Pipeline Phase 3 Patentablauf"
```

4. **Output Structure erweitern** (Zeile 165+):
```markdown
#### 3) Firma: [Name] – Portfolio-Kontext

[siehe Sektion 4 oben für vollständige Struktur]
```

### 5.2 Query-Strategies.md (falls vorhanden)

Ergänze in `~/.claude/skills/pharma-research/references/query-strategies.md`:

```markdown
## Company & Portfolio Research

### Goals
- Understand company financials and strategic priorities
- Map medication's position in portfolio
- Assess marketing investment willingness

### Query Templates

**Financial Overview:**
- "{Company} Pharma annual revenue EBITDA {Year}"
- "{Company} Geschäftsbericht {Year} Umsatz Gewinn"
- "{Company} stock market valuation market cap"

**Portfolio Mapping:**
- "{Company} top selling drugs products revenue"
- "{Company} blockbuster medications therapy areas"
- "{Company} patent cliff exclusivity expiry {Year}"

**Medication Revenue:**
- "{Drug} {Company} sales revenue {Year}"
- "{Drug} peak sales guidance forecast"
- "{Drug} launch performance uptake"

**Strategic Context:**
- "{Company} pipeline Phase 3 upcoming launches"
- "{Company} acquisition merger strategy"
- "{Company} {Drug} priority investment focus"
```

### 5.3 README.md Update

In `~/.claude/skills/pharma-research/README.md`:

**Usage Examples ergänzen:**
```markdown
### Example 3: Full Analysis with Company Context

**Query:**
```
Analyze the German pharmaceutical market for Psoriasis, Bimekizumab,
and UCB Pharma
```

**Result:**
- Complete indication analysis (epidemiology, unmet need, care pathway)
- Medication analysis (competition, differentiation, market access)
- **NEW:** Company portfolio analysis (UCB financials, Bimzelx position,
  strategic role)
- Investment priority scoring (5/5 stars)
- Marketing budget recommendation

**Cost:** ~$0.06-0.09 (8-10 searches @ "auto" mode)
```

---

## 6. Perplexity MCP Tool: Keine Änderungen nötig

Die bestehenden Tools `mcp__perplexity__perplexity_search` und
`mcp__perplexity__perplexity_social` unterstützen bereits:
- Deutsche Queries (`language: "de"`)
- Flexible query strings (können Firmennamen enthalten)
- Variable Token-Limits (1500-2000 für längere Analysen)

**Keine Code-Änderungen erforderlich** – nur neue Query-Formulierungen.

---

## 7. Testing-Strategie

### Test Case 1: Bekanntes Beispiel (Validation)
**Input:** "Analyze Psoriasis, Bimekizumab, UCB Pharma"

**Erwartete Outputs:**
- UCB Umsatz 6,15 Mrd. EUR (2024)
- Bimzelx Umsatz H1 2025: 799 Mio. EUR
- Peak Sales Guidance: >4 Mrd. EUR
- Portfolio-Anteil bei Peak: 40-50%
- Priorität: 5/5 (Growth Driver, kompensiert Cimzia-Patentverlust)

### Test Case 2: Kleinere Firma
**Input:** "Analyze Diabetes Type 2, Ozempic, Novo Nordisk"

**Erwartete Insights:**
- Novo Nordisk Fokus: Diabetes + Obesity
- Ozempic: Blockbuster (Teil der GLP-1 Familie mit Wegovy)
- Hoher Umsatzanteil (~30-40% des Portfolios)

### Test Case 3: Generika-Firma (Edge Case)
**Input:** "Analyze Hypertension, Ramipril, Ratiopharm"

**Erwartete Anpassung:**
- Niedrige Priorität (Generikum, kein Patentschutz)
- Geringer Umsatz pro Produkt
- Budgetempfehlung: Cost-efficient Pakete

---

## 8. Dokumentation

### Neue Dateien erstellen:
1. **`docs/COMPANY_ANALYSIS_GUIDE.md`**
   - Detaillierte Anleitung zur Firmenanalyse
   - Beispiel-Queries mit erwarteten Ergebnissen
   - Interpretation von Portfolio-Metriken

2. **`docs/examples/BIMZELX_UCB_EXAMPLE.md`**
   - Vollständiges Beispiel-Report
   - Zeigt alle drei Analyseebenen (Indikation, Medikament, Firma)

### Bestehende Dateien updaten:
- **`CLAUDE.md`** (Projekt-Root): Sektion "Pharma-Research Skill" um Firmenanalyse erweitern
- **`CHANGELOG.md`**: Neue Version mit Feature-Beschreibung

---

## 9. Rollout-Plan

### Phase 1: SKILL.md Update (30 Min)
- [ ] Neue Sektion "Part 3: Company & Portfolio Analysis" einfügen
- [ ] Query-Beispiele erweitern
- [ ] Output-Struktur anpassen

### Phase 2: Referenzdokumentation (45 Min)
- [ ] `query-strategies.md` erweitern (falls vorhanden)
- [ ] README.md updaten
- [ ] Beispiel-Report erstellen (Bimzelx/UCB)

### Phase 3: Testing (30 Min)
- [ ] Test Case 1: UCB/Bimzelx (bekannte Daten)
- [ ] Test Case 2: Novo Nordisk/Ozempic
- [ ] Test Case 3: Generika-Firma (Edge Case)

### Phase 4: Dokumentation (45 Min)
- [ ] `COMPANY_ANALYSIS_GUIDE.md` erstellen
- [ ] `CLAUDE.md` (Root) updaten
- [ ] `CHANGELOG.md` aktualisieren

**Geschätzte Gesamtzeit:** 2-3 Stunden

---

## 10. Offene Fragen / Entscheidungen

### Frage 1: Parameter-Extraktion
**Problem:** Wie soll die Skill Firmennamen aus User-Queries extrahieren?

**Option A (Recommended):** Explizite Nennung erforderlich
- User muss Firma nennen: "Analyze Psoriasis, Bimekizumab, UCB Pharma"
- Vorteil: Eindeutig, keine Fehler
- Nachteil: User muss Firma kennen

**Option B:** Automatische Extraktion
- Perplexity-Query: "Bimekizumab Hersteller" → extrahiere "UCB Pharma"
- Vorteil: User-freundlich
- Nachteil: Extra Query nötig (+$0.005 Kosten)

**Empfehlung:** Start mit Option A, später Option B als Fallback implementieren.

### Frage 2: Reporting-Detail-Grad
**Wie detailliert soll Portfolio-Analyse sein?**

**Option A:** Kompakt (wie in Sektion 4)
- 1 Seite zusätzlich im Report
- Fokus: Umsatz, Priorität, Marketing-Implikation

**Option B:** Ausführlich
- 2-3 Seiten mit allen Top-10-Produkten im Portfolio
- Detaillierte Pipeline-Analyse
- Vergleich mit Wettbewerber-Portfolios

**Empfehlung:** Start mit Option A (Kompakt). User können bei Bedarf Detailfragen stellen.

### Frage 3: Kosten-Optimierung
**Mit Firmendaten steigen Searches von 5-6 auf 8-10 → Kosten +30-50%**

**Aktuelle Kosten:** ~$0.03-0.045 pro Report
**Neue Kosten:** ~$0.06-0.09 pro Report

**Optimierung möglich?**
- Option 1: `search_type="fast"` für Firmen-Basics (reicht für Umsatz)
- Option 2: Firmenanalyse optional (nur wenn explizit requested)

**Empfehlung:** Immer durchführen (Mehrwert rechtfertigt +$0.03), aber `fast` für
reine Fakten-Queries (Firmenumsatz) nutzen.

---

## 11. Zusammenfassung

**Was wird erweitert:**
- Neue Analyse-Dimension: Firma & Portfolio-Kontext
- 3-4 zusätzliche Perplexity-Queries pro Report
- Neue Output-Sektion: "3) Firma: [Name] – Portfolio-Kontext"
- Investment-Priorität-Scoring (1-5 Sterne)
- Marketing-Budget-Empfehlungen basierend auf Portfolio-Position

**Was bleibt gleich:**
- Bestehende Indikations- und Medikamenten-Analysen
- Perplexity MCP Tool (keine Code-Änderungen)
- Deutsche Sprache für Queries
- Markdown-Output mit Quellen

**Nutzen für dich als Analyst:**
- Verstehe sofort, ob ein Medikament "Blockbuster-Launch" oder "Maintenance-Produkt" ist
- Erkenne Verhandlungspositionen (Patentdruck, Portfoliolücken)
- Tailiere Angebote nach Investment-Bereitschaft der Firma

**Kosten-Impact:**
- +3-4 Perplexity-Queries pro Analyse
- +$0.03-0.045 pro Report (~+60% Kosten)
- Neue Kosten: ~$0.06-0.09 pro vollständigem Report

---

## Nächste Schritte

1. **Review dieses Plans** – Feedback geben zu:
   - Ist die Analyse-Tiefe richtig? (Sektion 2)
   - Passen die Queries? (Sektion 3)
   - Ist die Output-Struktur klar? (Sektion 4)

2. **Entscheidungen treffen:**
   - Frage 1: Parameter-Extraktion (Option A vs. B)
   - Frage 2: Detail-Grad (Kompakt vs. Ausführlich)
   - Frage 3: Kosten-Optimierung (Always-on vs. Optional)

3. **Implementierung starten:**
   - Ich kann direkt mit Phase 1 (SKILL.md Update) beginnen
   - Oder erst ein Mock-up Report erstellen zur Validierung

**Was möchtest du als Erstes?**
