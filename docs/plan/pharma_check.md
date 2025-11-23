ich bin ein analyst, der für eine Firma in Berlin arbeitet, die digitales Pharmamarketing abwickelt. Eine Plattform für Ärzte, auf der Microsites oder BAnner geschlatet werden. Es werden Newsletter versendet. Ich hätte gern eine Möglichkeit zu verstehen, dass wenn eine Pharmafirma auf uns zukommt mit einem Medikament - dann würde ich gern verstehen, welche Rolle dieses Medikament in ihrem Portfolio spielt. Das ist ziemlich komplex, hat mit Profit und Loss zu tun und den anderen Business Units in der Firma, es würde wahrscheinlich auch beinhalten, welche Historie die Firma hat, ob sie zu einem noch größeren Konzern gehört, etc.

Ich arbeite mit Claude Code, habe die API Keys der größten AI Provider zur Verfügung, begrenzt auch Perplexity. Hast du einen Vorschlag für mich?

Strategischer Ansatz: Pharma-Portfolio-Analyse
Konzept
Mehrstufiges Research-System, das:

Grunddaten sammelt (Produkt, Hersteller, Indikation)
Kontext aufbaut (Konzernstruktur, Portfolio, Finanzdaten)
Strategische Einordnung ableitet (Produktrolle, Lifecycle, Priorisierung)
Empfohlene Architektur
Eingabe: Medikament/Hersteller
    ↓
[1] Perplexity: Schnelle Faktensammlung
    - Wirkstoff, Indikation, Zulassung
    - Hersteller, Konzernzugehörigkeit
    ↓
[2] Claude API: Strukturierte Weiterrecherche
    - Pipeline-Analyse (Phase 3/4 Trials)
    - Patentablauf, Biosimilar-Risiko
    - Umsatzzahlen (Geschäftsberichte)
    ↓
[3] Claude Code: Synthese & Scoring
    - Portfolio-Matrix (Umsatz vs. Wachstum)
    - Strategische Einordnung
    - Output: Markdown-Report
Implementierungsvorschlag
Tool-Stack:

Perplexity API → Initiale Recherche (3-5 Queries)
Claude Sonnet 4.5 → Deep Analysis (Geschäftsberichte, Pipeline-Daten)
Claude Code → Orchestrierung, Datenintegration, Report-Generierung
Workflow in Claude Code:

python
# pseudo_code.py
def analyze_drug_portfolio(drug_name, company_name):
    # Phase 1: Perplexity für Basisfacts
    basic_info = perplexity_search([
        f"{drug_name} Wirkstoff Indikation",
        f"{company_name} Konzernstruktur Umsatz",
        f"{drug_name} Patentablauf Marktgröße"
    ])
    
    # Phase 2: Claude für Kontext-Analyse
    context = claude_analyze(
        prompt=f"Analysiere Geschäftsbericht und Pipeline von {company_name}",
        sources=basic_info
    )
    
    # Phase 3: Scoring & Einordnung
    report = generate_report({
        'product_lifecycle': classify_lifecycle(basic_info),
        'revenue_share': calculate_share(context),
        'strategic_priority': score_priority(context)
    })
    
    return report  # Markdown mit Matrix + Empfehlungen
Konkrete Fragen für dich:
Datenquellen: Hast du Zugang zu Pharma-Datenbanken (Evaluate, IQVIA) oder nur öffentliche Quellen?
Frequenz: Einmalige Analyse oder regelmäßiges Monitoring?
Output: Reicht ein strukturierter Markdown-Report oder brauchst du ein Dashboard?
Soll ich einen funktionierenden Prototyp in Claude Code bauen?

Nur öffentliche Quellen, kein IQVIA
2) einmalig
3 markdown reicht aus

Implementierung
Setup-Plan
python
# research_agent.py - Hauptskript in Claude Code

import anthropic
import requests
import json
from datetime import datetime

class PharmaPortfolioAnalyzer:
    def __init__(self, perplexity_key, anthropic_key):
        self.pplx = perplexity_key
        self.claude = anthropic.Anthropic(api_key=anthropic_key)
    
    def analyze(self, drug_name, company_name):
        # 1. Perplexity: Schnelle Fakten
        basic_facts = self._perplexity_research(drug_name, company_name)
        
        # 2. Claude: Deep Analysis
        analysis = self._claude_deep_dive(basic_facts)
        
        # 3. Report generieren
        return self._generate_markdown(analysis)
Phase 1: Perplexity Queries
python
def _perplexity_research(self, drug, company):
    queries = [
        f"{drug} Wirkstoff Indikation Zulassung Deutschland Europa",
        f"{company} Mutterkonzern Pharma Portfolio Umsatz Geschäftsbericht",
        f"{drug} {company} Umsatz Marktanteil Patentablauf",
        f"{company} Pipeline Medikamente Entwicklung Phase 3"
    ]
    
    results = []
    for q in queries:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={"Authorization": f"Bearer {self.pplx}"},
            json={
                "model": "sonar",
                "messages": [{"role": "user", "content": q}]
            }
        )
        results.append(response.json())
    
    return results
Phase 2: Claude Strukturierung
python
def _claude_deep_dive(self, raw_data):
    prompt = f"""Analysiere diese Recherche-Ergebnisse zu einem Pharma-Produkt:

{json.dumps(raw_data, indent=2)}

Erstelle eine strukturierte Analyse als JSON:
{{
  "product": {{
    "name": "...",
    "active_ingredient": "...",
    "indication": "...",
    "approval_status": "...",
    "patent_expiry": "YYYY oder 'unknown'"
  }},
  "company": {{
    "name": "...",
    "parent_corporation": "... oder 'independent'",
    "total_revenue_eur": "Zahl oder null",
    "therapeutic_areas": ["area1", "area2"]
  }},
  "portfolio_position": {{
    "product_revenue_eur": "Zahl oder null",
    "revenue_share_percent": "Zahl oder null",
    "lifecycle_stage": "launch|growth|mature|decline",
    "competitors": ["prod1", "prod2"],
    "market_size_eur": "Zahl oder null"
  }},
  "strategic_assessment": {{
    "priority_score": "1-5 (5=höchste Priorität)",
    "rationale": "2-3 Sätze Begründung",
    "marketing_implications": "Empfehlung für Kampagnenbudget"
  }}
}}

Nur JSON ausgeben, keine Markdown-Formatierung."""

    response = self.claude.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return json.loads(response.content[0].text)
Phase 3: Markdown Report
python
def _generate_markdown(self, data):
    p = data['product']
    c = data['company']
    pos = data['portfolio_position']
    strat = data['strategic_assessment']
    
    return f"""# Portfolio-Analyse: {p['name']}

**Datum:** {datetime.now().strftime('%Y-%m-%d')}

## 1. Produkt-Übersicht

| Attribut | Wert |
|----------|------|
| Wirkstoff | {p['active_ingredient']} |
| Indikation | {p['indication']} |
| Zulassung | {p['approval_status']} |
| Patentablauf | {p['patent_expiry']} |

## 2. Hersteller-Kontext

**{c['name']}** {'(Teil von ' + c['parent_corporation'] + ')' if c['parent_corporation'] != 'independent' else ''}

- Gesamtumsatz: {c['total_revenue_eur']} Mio. EUR
- Therapiegebiete: {', '.join(c['therapeutic_areas'])}

## 3. Portfolio-Position
```
Lifecycle: {pos['lifecycle_stage'].upper()}
Produktumsatz: {pos['product_revenue_eur']} Mio. EUR ({pos['revenue_share_percent']}% des Portfolios)
Marktgröße: {pos['market_size_eur']} Mio. EUR
```

**Wettbewerber:** {', '.join(pos['competitors'])}

## 4. Strategische Einordnung

**Priorität:** {'⭐' * int(strat['priority_score'])} ({strat['priority_score']}/5)

{strat['rationale']}

### Empfehlung Marketing-Budget
{strat['marketing_implications']}

---
*Generiert mit öffentlichen Quellen via Perplexity + Claude*"""
Nutzung in Claude Code
bash
# In deinem Terminal mit Claude Code
python research_agent.py --drug "Ozempic" --company "Novo Nordisk"
Fragen:

Soll ich das vollständige Skript als .py-Datei vorbereiten?
Brauchst du zusätzlich eine Visualisierung (Portfolio-Matrix als ASCII/SVG)?
Lass uns das mal am Beispiel Bimekizumab machen. Kannst du Portfolio infos dazu finden, kannst du rausfinden, welche Pharma firma das ist zuerst?


Bimekizumab Hersteller Pharmafirma
10 Ergebnisse





















Perfekt! Bimekizumab (Handelsname Bimzelx) wird von UCB Pharma hergestellt. 
Pharmazeutische Zeitung
PatientenInfo-Service

Jetzt suche ich weitere Portfolio-Informationen zu UCB:


1 Schritt

UCB Pharma wichtigste Medikamente Cimzia Keppra
10 Ergebnisse






















Bimzelx Bimekizumab Umsatz 2024 revenue sales
10 Ergebnisse





















Sehr gut! Jetzt suche ich noch nach weiteren Portfolio-Informationen und der strategischen Bedeutung von Bimzelx:


UCB Pharma Patentablauf Bimzelx patent expiry
10 Ergebnisse





















Perfekt! Ich habe jetzt genug Informationen gesammelt. Lass mich eine Portfolio-Analyse erstellen:

Portfolio-Analyse: Bimekizumab (Bimzelx)
Stand: November 2025

1. Produkt-Übersicht
Attribut	Wert
Wirkstoff	Bimekizumab
Handelsname	Bimzelx
Wirkmechanismus	IL-17A und IL-17F Inhibitor (dual)
Indikationen	Plaque-Psoriasis, Psoriasis-Arthritis, Axiale Spondyloarthritis, Hidradenitis suppurativa
Zulassung EU	August 2021
Zulassung USA	Oktober 2023
Patentablauf	USA: 2035, EU: 2036, Japan: 2037
2. Hersteller-Kontext
UCB Pharma S.A. (Hauptsitz: Brüssel, Belgien)

Gesamtumsatz 2024: 6,15 Mrd. EUR 
Ucb
Lobbyregister beim Deutschen Bundestag
Mitarbeiter: >9.000 weltweit 
Lobbyregister beim Deutschen Bundestag
Gegründet: 1928 
Wikipedia
Konzernstruktur: Unabhängiges, börsennotiertes Unternehmen (Euronext Brussels)
Fokus: Neurologie, Immunologie, Seltene Erkrankungen 
Lobbyregister beim Deutschen Bundestag
Ucb
F&E-Quote: 29% des Umsatzes (2024) 
Lobbyregister beim Deutschen Bundestag
Wichtigste Produkte im Portfolio:

Keppra (Levetiracetam) - Epilepsie - historisch umsatzstärkstes Produkt 
Wikipedia
Cimzia (Certolizumab) - Rheumatoide Arthritis, Morbus Crohn 
Wikipedia
Wikipedia
Vimpat (Lacosamide) - Epilepsie
Briviact (Brivaracetam) - Epilepsie
Evenity (Romosozumab) - Osteoporose (Co-Marketing mit Amgen)
Fintepla (Fenfluramine) - Seltene Epilepsie-Formen
Rystiggo, Zilbrysq - Myasthenia gravis
3. Portfolio-Position von Bimzelx
Umsatzentwicklung
2023: ~150 Mio. EUR (Wachstum +323%)
H1 2024: 215 Mio. EUR
2024 gesamt: geschätzt ~500 Mio. EUR
H1 2025: 799 Mio. EUR
Bimzelx zeigt dreistelliges Wachstum und gehört zu UCBs "Growth Drivers" neben Evenity, Fintepla, Rystiggo und Zilbrysq. 
On Growth Path for a Decade plus: Strong Launch Execution driving Company Growth | UCB +2

Marktposition & Lifecycle
Lifecycle-Stage: Launch/Growth (frühes Wachstum)

Peak Sales Guidance: >4 Mrd. EUR 
UCB
Bereits >82.000 Patienten weltweit (April 2025) 
UCB
In 47 Ländern für Psoriasis verfügbar, >40 Länder für weitere Indikationen 
UCB
Marktgröße & Wettbewerb:

Hauptkonkurrenten: Novartis Cosentyx (Secukinumab), AbbVie Skyrizi, Eli Lilly Taltz (Ixekizumab)
Globaler Bimekizumab-Markt 2024: 1,24 Mrd. USD, Prognose 2034: 8,1 Mrd. USD (CAGR 20,6%) 
Precedence Research
Alleinstellungsmerkmal: Einziger dualer IL-17A/IL-17F Inhibitor (bessere Wirksamkeit als reine IL-17A-Hemmer)
Strategische Bedeutung
Priorität: ⭐⭐⭐⭐⭐ (5/5)

Begründung:

Kompensation für Patentverluste: Bimzelx soll Umsatzeinbußen durch auslaufende Patente von Cimzia (2024) und Vimpat (2022) ausgleichen 
Evaluate
Wachstumstreiber: UCB positioniert sich für "Dekade des Wachstums" mit Bimzelx als Flaggschiff 
UCB
Fierce Pharma
Indikationserweiterung: 2024: 5 FDA-Zulassungen in den USA (Psoriasis, PsA, nr-axSpA, AS, Hidradenitis suppurativa) 
UCB
UCB
Umsatzanteil: Bei Peak Sales von >4 Mrd. EUR würde Bimzelx ~40-50% des Gesamtumsatzes ausmachen (aktuell Gesamtumsatz 6,15 Mrd. EUR)
4. Marketing-Empfehlungen
Budget-Allokation
Hoch-Priorität Kampagne empfohlen:

Phase: Aggressiver Launch in Schlüsselmärkten (USA, Deutschland, UK)
Zielgruppe: Dermatologen, Rheumatologen, Fachärzte für Immunologie
UCB startete 2024 Direct-to-Consumer Kampagne in den USA 
Fierce Pharma
Kanäle:
Fachärzte-Newsletter (Dermatologie, Rheumatologie)
Kongress-Präsenz (AAD, EADV, ACR)
Digitale Microsites mit Real-World Evidence Daten
Patient Support Programme
Positionierung
Kernbotschaften:

"Einziger dualer IL-17A/17F Inhibitor"
Höchste PASI90/100 Raten (84-93% erscheinungsfreie Haut) 
Pharmazeutische Zeitung
Schnelles Ansprechen + anhaltende Wirkung über 2+ Jahre
Flexible Dosierung (Q4W/Q8W je nach Indikation)
Timing-Strategie
Jetzt zuschlagen:

Patentschutz bis 2035-2037 = Langfristige Exklusivität 
UCB
Vor Markteintritt weiterer IL-17F-Inhibitoren (z.B. Acelyrin's Izokibep in 2-3 Jahren)
UCB investiert massiv in Launch-Aktivitäten (23-24% EBITDA-Marge wegen Launch-Kosten)
Zusammenfassung: Bimzelx ist UCBs strategisches Kronjuwel zur Sicherung der Unternehmenszukunft. Als Pharmafirma, die auf euch zukommt, signalisiert dies höchste Investitionsbereitschaft in Marketing-Aktivitäten. Das Produkt befindet sich in der kritischen Launch-Phase mit aggressivem Wachstumsziel (4 Mrd. EUR Peak Sales = Blockbuster-Potenzial).