# esanum analytics – Word Document Design Guidelines

## Purpose

These guidelines ensure consistent, professional Word documents for esanum analytics. Apply them when creating .docx files using the docx skill.

---

## Color System

Use only grayscale variations of `#444444`. This creates a calm, professional appearance.

| Role | Hex Code | Usage |
|------|----------|-------|
| **Primary Text** | `#444444` | Body text, headlines, table content |
| **Secondary Text** | `#666666` | Subheadlines (H2, H3) |
| **Muted Text** | `#888888` | Footer, metadata, captions |
| **Borders** | `#DDDDDD` | Table borders, dividers |

**Do not use:**
- Brand colors in document body
- Colored backgrounds
- Alternating row colors in tables

---

## Logo

**File:** `esanum_analytics_grey.png`

> **IMPORTANT:** The logo must NEVER be distorted. Always preserve the original aspect ratio.

**Original Dimensions:**
- Source file: 1579 × 284 pixels
- Aspect ratio: **5.56:1** (width:height)

**How to Calculate Correct Size:**
1. Decide on desired height (e.g., 27px for documents)
2. Multiply height by 5.56 to get width
3. Example: height 27px → width = 27 × 5.56 = **150px**

**Placement:**
- Position: Header, top-left
- Recommended size: **150px width × 27px height** (or any size maintaining 5.56:1 ratio)
- Add generous spacing below logo (minimum 300 twips)

**CRITICAL - Do not:**
- Set width and height independently without calculating the ratio
- Stretch or compress the logo in any direction
- Use arbitrary dimensions that don't match 5.56:1
- Place content too close to the logo

---

## Typography

**Font:** Arial (universal compatibility)

| Element | Size | Weight | Color | Spacing (before/after) |
|---------|------|--------|-------|------------------------|
| **Document Title** | 13pt (26) | Bold | #444444 | 400/200 |
| **H1** | 11pt (22) | Bold | #444444 | 300/150 |
| **H2** | 9pt (18) | Bold | #666666 | 200/100 |
| **H3** | 8pt (16) | Bold | #666666 | 160/80 |
| **Body Text** | 8pt (16) | Regular | #444444 | 60/60 |
| **Bullet Points** | 8pt (16) | Regular | #444444 | 40/40 |
| **Footer** | 7pt (14) | Regular | #888888 | — |

*Sizes in parentheses are half-points (docx-js format)*

---

## Tables

Tables should be understated and not dominate the page.

**Principles:**
- Use auto-width (`WidthType.AUTO`) – tables size to content, not full page width
- No background colors (all cells white)
- Uniform light borders (`#DDDDDD`, 1pt)
- Adequate cell padding (60 twips before/after)

**Header Row:**
- Bold text, same color as body (#444444)
- No background shading
- Same border style as data rows

**Do not:**
- Use dark header backgrounds
- Apply alternating row colors
- Force tables to full page width

---

## Page Layout

| Property | Value |
|----------|-------|
| **Top Margin** | 1200 twips (~21mm) |
| **Side Margins** | 720 twips (~13mm) |
| **Bottom Margin** | 720 twips (~13mm) |

**Footer:**
- Centered
- Format: `esanum analytics | [Document Title] | Seite X von Y`
- Color: #888888

---

## Content Hierarchy

Structure documents with clear visual hierarchy:

1. **Document Title** – One per document, at top
2. **H1** – Major sections (numbered: 1., 2., 3.)
3. **H2** – Subsections within major sections
4. **H3** – Minor subsections or table labels
5. **Body Text** – Paragraphs, explanations
6. **Bullet Points** – Lists, key points
7. **Tables** – Structured data

**Spacing principle:** More important elements get more surrounding space.

---

## Lists

**Bullet Points:**
- Use standard bullet character (•)
- Indent: 280 twips
- Consistent spacing (40/40 twips)

**Numbered Lists:**
- Use for sequential steps or ranked items
- Same indent and spacing as bullets

---

## Implementation Notes (docx-js)

```javascript
// Color constants
const TEXT_DARK = "444444";
const TEXT_MID = "666666";
const TEXT_LIGHT = "888888";
const BORDER_LIGHT = "DDDDDD";

// Table with auto-width
new Table({
    width: { size: 0, type: WidthType.AUTO },
    rows: [/* ... */]
});

// Logo in header with spacing
new Header({
    children: [new Paragraph({
        spacing: { after: 300 },
        children: [new ImageRun({
            type: "png",
            data: logoBuffer,
            transformation: { width: 150, height: 27 }
        })]
    })]
});
```

---

## Quality Checklist

Before finalizing a document:

- [ ] Logo appears correctly with proper spacing
- [ ] All text uses only #444444 / #666666 / #888888
- [ ] Tables are appropriately sized (not stretched)
- [ ] No colored backgrounds anywhere
- [ ] Consistent heading hierarchy
- [ ] Footer displays correctly with page numbers
- [ ] Content matches source document exactly (nothing added or removed)

---

*These guidelines prioritize readability, professionalism, and reproducibility.*
