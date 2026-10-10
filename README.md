# Factors Affecting Commuter Mode Choice (Bengaluru)

A questionnaire survey of how Bengaluru commuters choose between metro, bus, two-wheeler, car, cab and auto, and what keeps them off public transport. Includes the survey data, the analysis scripts, 12 figures and the final report.

## Key findings

- **Namma Metro is the top mode (43%)**, followed by BMTC bus (17%), two-wheeler (13%) and cab (13%).
- 53% commute more than 46 minutes one way, and 60% of trips are 8–25 km.
- **83% of vehicle owners still use public or shared transport.** 80% of high-income respondents prefer the metro: reliability wins riders.
- Top suggestion from respondents: increase BMTC bus frequency. Further recommendations cover last-mile connectivity and fare integration.

## Method

- **Sample:** N = 30, stratified across metro stations, bus stops and IT hubs.
- **Instrument:** Google Form covering demographics, income, vehicle ownership, trip purpose, mode, time, cost, satisfaction and barriers to public transport (see `report/survey_instrument.pdf`).
- **Analysis:** descriptive statistics and cross-tabulations (mode by age, income and purpose) in Python.

## Repository structure

```
code/
├── 01_descriptive_analysis.py   summary statistics → *_summary.csv
└── 02_visualizations.py         12 figures + viz_*.csv cross-tabs
data/survey_responses.csv        anonymous survey responses
results/
├── figures/                     fig1–fig12 (mode share, satisfaction, heatmaps, ...)
└── tables/                      summary and cross-tab CSVs
report/
├── final_report.pdf
└── survey_instrument.pdf
```

## Getting started

```bash
pip install -r requirements.txt
cd code
python 01_descriptive_analysis.py
python 02_visualizations.py
```

Both scripts read `../data/survey_responses.csv` and write their outputs to the current folder. The committed outputs are in `results/`.

## Team

SL 221 Introduction to Multimodal Mobility Systems, Indian Institute of Science (IISc), Nov 2025.
Anant Rajput, Yakshith Maddineni, Soham Chakraborty, Ashish Kumar Verma.
