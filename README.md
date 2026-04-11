# Sales Analytics Dashboard

An interactive business intelligence dashboard analysing **541,909 retail transactions** across 37 countries, built from scratch using Python and vanilla JavaScript.

## What's Inside

```
sales-dashboard/
├── data/
│   ├── data.csv               # Raw dataset (Online Retail)
│   └── dashboard_data.json    # Pre-processed output (auto-generated)
├── analysis.py                # Data cleaning & aggregation (Python/pandas)
├── dashboard.html             # Interactive dashboard (Chart.js)
├── serve.py                   # Local dev server
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the analysis
```bash
python analysis.py
```
This cleans the raw CSV and outputs `data/dashboard_data.json`.

### 3. Launch the dashboard
```bash
python serve.py
```
Opens automatically at `http://localhost:8000/dashboard.html`

---

## Key Findings

| Metric | Value |
|--------|-------|
| Total Revenue | £8.91M |
| Total Orders | 18,536 |
| Avg Order Value | £481 |
| Peak Month | November 2011 |
| Countries | 37 |

### Insights
- **Seasonal surge**: Revenue grew 80% from Aug → Nov 2011 (holiday gifting)
- **UK dominance**: 82% of revenue from UK; Netherlands, Germany, France are top international markets
- **Top SKU**: *Paper Craft, Little Birdie* generated £168K alone
- **Anonymous buyers**: 25% of transactions had no CustomerID — a key retention opportunity

---

## Tech Stack
- **Python** (pandas) — data cleaning & analysis
- **JavaScript** (Chart.js 4.4) — interactive visualisations
- **HTML/CSS** — dashboard UI

## Dataset
[Online Retail Dataset](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset) — Kaggle
