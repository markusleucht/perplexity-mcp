#!/usr/bin/env python3
"""
Prompt enrichment module for Perplexity deep research.

Follows Perplexity best practices:
- "Think like a web search user" - use terms that appear on relevant pages
- "Avoid overly generic questions" - narrow scope with specific terms
- Include searchable entities (drug names, manufacturers, indications)
"""

import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime

# Known pharmaceutical entities for enrichment
DRUG_DATABASE = {
    # Dermatology
    "bimzelx": {"generic": "Bimekizumab", "manufacturer": "UCB", "class": "IL-17A/F Inhibitor"},
    "cosentyx": {"generic": "Secukinumab", "manufacturer": "Novartis", "class": "IL-17A Inhibitor"},
    "skyrizi": {"generic": "Risankizumab", "manufacturer": "AbbVie", "class": "IL-23 Inhibitor"},
    "tremfya": {"generic": "Guselkumab", "manufacturer": "Janssen", "class": "IL-23 Inhibitor"},
    "humira": {"generic": "Adalimumab", "manufacturer": "AbbVie", "class": "TNF-alpha Inhibitor"},
    "taltz": {"generic": "Ixekizumab", "manufacturer": "Lilly", "class": "IL-17A Inhibitor"},
    "stelara": {"generic": "Ustekinumab", "manufacturer": "Janssen", "class": "IL-12/23 Inhibitor"},

    # Diabetes/Obesity
    "ozempic": {"generic": "Semaglutid", "manufacturer": "Novo Nordisk", "class": "GLP-1 Agonist"},
    "wegovy": {"generic": "Semaglutid", "manufacturer": "Novo Nordisk", "class": "GLP-1 Agonist"},
    "mounjaro": {"generic": "Tirzepatid", "manufacturer": "Lilly", "class": "GIP/GLP-1 Agonist"},
    "trulicity": {"generic": "Dulaglutid", "manufacturer": "Lilly", "class": "GLP-1 Agonist"},
    "jardiance": {"generic": "Empagliflozin", "manufacturer": "Boehringer Ingelheim", "class": "SGLT2 Inhibitor"},
    "forxiga": {"generic": "Dapagliflozin", "manufacturer": "AstraZeneca", "class": "SGLT2 Inhibitor"},

    # Oncology
    "keytruda": {"generic": "Pembrolizumab", "manufacturer": "MSD", "class": "PD-1 Inhibitor"},
    "opdivo": {"generic": "Nivolumab", "manufacturer": "BMS", "class": "PD-1 Inhibitor"},
    "tecentriq": {"generic": "Atezolizumab", "manufacturer": "Roche", "class": "PD-L1 Inhibitor"},
    "imfinzi": {"generic": "Durvalumab", "manufacturer": "AstraZeneca", "class": "PD-L1 Inhibitor"},

    # Cardiology
    "entresto": {"generic": "Sacubitril/Valsartan", "manufacturer": "Novartis", "class": "ARNI"},
    "eliquis": {"generic": "Apixaban", "manufacturer": "BMS/Pfizer", "class": "DOAC"},
    "xarelto": {"generic": "Rivaroxaban", "manufacturer": "Bayer", "class": "DOAC"},
}

# Indication terms with German equivalents
INDICATION_TERMS = {
    "psoriasis": "Psoriasis Schuppenflechte plaque moderate-to-severe mittelschwer schwer",
    "diabetes": "Diabetes mellitus Typ 2 T2DM Blutzucker HbA1c",
    "obesity": "Adipositas Uebergewicht Gewichtsmanagement BMI",
    "herzinsuffizienz": "Herzinsuffizienz HFrEF HFpEF Herzschwaeche kardial",
    "heart failure": "Herzinsuffizienz HFrEF HFpEF heart failure",
    "cancer": "Krebs Onkologie Tumor Karzinom",
    "rheumatoid arthritis": "Rheumatoide Arthritis RA Rheuma autoimmun",
    "atopic dermatitis": "Atopische Dermatitis Neurodermitis Ekzem",
    "crohn": "Morbus Crohn CED IBD Darm entzuendlich",
    "colitis": "Colitis ulcerosa CED IBD Darm",
}

# Pharma market research context keywords (German)
PHARMA_CONTEXT_KEYWORDS = """
Deutschland German market Markt
Epidemiologie Praevalenz Inzidenz Patientenpopulation
Wettbewerb Konkurrenz Marktanteil market share
Verschreiber Facharzt HCP prescriber
Portfolio Produktzyklus lifecycle
Marketing Positionierung positioning
Erstattung reimbursement GKV
Zulassung approval EMA BfArM
klinische Studien clinical trials Phase III
Wirkmechanismus mechanism of action MoA
Differenzierung differentiation USP
""".strip()


def detect_entities(query: str) -> Dict[str, any]:
    """
    Detect pharmaceutical entities in the query.

    Returns dict with detected drugs, indications, and manufacturers.
    """
    query_lower = query.lower()
    entities = {
        "drugs": [],
        "indications": [],
        "manufacturers": [],
    }

    # Detect drugs
    for drug_name, info in DRUG_DATABASE.items():
        if drug_name in query_lower or info["generic"].lower() in query_lower:
            entities["drugs"].append({
                "brand": drug_name.capitalize(),
                "generic": info["generic"],
                "manufacturer": info["manufacturer"],
                "class": info["class"],
            })

    # Detect indications
    for indication, terms in INDICATION_TERMS.items():
        if indication in query_lower:
            entities["indications"].append({
                "name": indication,
                "search_terms": terms,
            })

    # Detect manufacturers mentioned
    manufacturers = ["ucb", "novartis", "abbvie", "lilly", "novo nordisk",
                    "janssen", "msd", "bms", "roche", "astrazeneca",
                    "bayer", "pfizer", "boehringer", "sanofi", "gsk"]
    for mfr in manufacturers:
        if mfr in query_lower:
            entities["manufacturers"].append(mfr.title())

    return entities


def is_pharma_query(query: str) -> bool:
    """Detect if query is pharmaceutical/healthcare related."""
    pharma_indicators = [
        "drug", "medication", "pharma", "therapeutic", "clinical",
        "patient", "treatment", "therapy", "indication", "approval",
        "medikament", "arzneimittel", "therapie", "behandlung",
        "zulassung", "markt", "verschreiber", "facharzt",
    ]
    query_lower = query.lower()

    # Check for known drugs
    for drug in DRUG_DATABASE.keys():
        if drug in query_lower:
            return True

    # Check for pharma indicators
    for indicator in pharma_indicators:
        if indicator in query_lower:
            return True

    return False


def enrich_query(
    query: str,
    context_hint: Optional[str] = None,
    skip_enrichment: bool = False,
) -> Tuple[str, Dict]:
    """
    Enrich user query with search-optimized terms.

    Follows Perplexity best practices:
    - Use specific, searchable terms
    - Include relevant entities and synonyms
    - Add temporal and geographic context

    Args:
        query: Original user query
        context_hint: Optional hint ("pharma", "market", "tech", etc.)
        skip_enrichment: If True, return query unchanged

    Returns:
        Tuple of (enriched_query, metadata_dict)
    """
    if skip_enrichment:
        return query, {"enriched": False, "original": query}

    enrichments = []
    metadata = {
        "enriched": True,
        "original": query,
        "entities_detected": {},
        "context_applied": [],
    }

    # 1. Temporal context (always: last 5 years as specified)
    current_year = datetime.now().year
    temporal = f"{current_year - 5}-{current_year} aktuell current latest"
    enrichments.append(temporal)
    metadata["context_applied"].append("temporal_5yr")

    # 2. Geographic context (always: Germany as specified)
    geo = "Deutschland Germany German deutscher Markt"
    enrichments.append(geo)
    metadata["context_applied"].append("geo_germany")

    # 3. Detect and expand entities
    entities = detect_entities(query)
    metadata["entities_detected"] = entities

    # Expand drug information
    for drug in entities["drugs"]:
        drug_expansion = f"{drug['brand']} ({drug['generic']}) {drug['manufacturer']} {drug['class']}"
        enrichments.append(drug_expansion)

    # Expand indication information
    for indication in entities["indications"]:
        enrichments.append(indication["search_terms"])

    # 4. Apply context-specific enrichments
    auto_pharma = is_pharma_query(query)
    if context_hint == "pharma" or auto_pharma:
        enrichments.append(PHARMA_CONTEXT_KEYWORDS)
        metadata["context_applied"].append("pharma_market")

    # 5. Build enriched query
    enrichment_block = " ".join(enrichments)
    enriched = f"""{query}

Recherche-Kontext (fuer Suchoptimierung):
{enrichment_block}"""

    return enriched, metadata


def get_pharma_system_context() -> str:
    """
    Return the fixed pharma audience context.

    As specified: Sales executives in a pharma marketing agency (Berlin)
    dealing with omnichannel/online marketing managers in Big Pharma.
    """
    return """Kontext: Diese Recherche ist fuer eine Pharma-Marketing-Agentur in Berlin,
die Big-Pharma-Unternehmen zu Omnichannel- und Online-Marketing beraet.

Die Zielgruppe sind Vertriebsleiter, die verstehen muessen:
- Das Produkt selbst (Wirkmechanismus, Differenzierung, klinisches Profil)
- Marktpotenzial in Deutschland (Patientenpopulation, Wachstum, Wettbewerb)
- Relevanz im Herstellerportfolio (strategische Bedeutung, Lebenszyklusphase)
- Marketing-Beratungspotenzial (Positionierung, Ziel-HCPs, Kampagnenansaetze)"""


if __name__ == "__main__":
    # Test the enrichment
    test_queries = [
        "Analysiere Bimzelx fuer Psoriasis von UCB",
        "What is the market share of Ozempic in Germany?",
        "Wie entwickelt sich der deutsche E-Auto-Markt?",
    ]

    print("Testing prompt enrichment:\n")
    for q in test_queries:
        enriched, meta = enrich_query(q)
        print(f"Original: {q}")
        print(f"Pharma detected: {is_pharma_query(q)}")
        print(f"Entities: {meta['entities_detected']}")
        print(f"Enriched query:\n{enriched[:300]}...")
        print("-" * 50)
