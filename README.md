# Diabetes Risk Prediction from CDC Health Indicators

Predict diabetes risk from self-reported health survey indicators using cleaning, classical statistics, and baseline ML models (logistic regression + SVM).

Built as a **5-person** machine learning project on a cleaned **70,692-record** CDC health survey dataset with **21** indicators.

## Highlights

- Cleaned and validated a large CDC survey extract in **Python / Pandas** (corrupted features + missing values)
- Ran **chi-squared**, **two-sample t-tests**, and **Mann-Whitney U** tests across 21 indicators
- Found **BMI, blood pressure, cholesterol, and age** as significant predictors of diabetes
- Authored the primary analysis write-up for **logistic regression** and **SVM** results

## Motivation

Diabetes screening at population scale is expensive if it depends only on clinical labs. Survey-based indicators from the CDC’s Behavioral Risk Factor Surveillance System (BRFSS) are widely used for public-health risk modeling. This project asks which of those indicators associate with diabetes status, and how well simple, interpretable models recover that signal.

## Dataset

| Item | Detail |
| --- | --- |
| Source | CDC BRFSS health indicators (diabetes risk / binary diabetes label) |
| Rows after cleaning | 70,692 |
| Features | 21 health indicators |
| Target | Diabetes status (binary) |

> **Do not commit the raw CSV.** Place it in `data/raw/` locally (gitignored). Prefer linking the public CDC/BRFSS or Kaggle mirror you actually used.

Common public mirrors (confirm which one you used, then document the exact year/file):
- [CDC BRFSS annual data](https://www.cdc.gov/brfss/annual_data/annual_data.htm)
- Community extracts such as the BRFSS diabetes health indicators datasets on Kaggle

## Repo layout

```text
diabetes-risk-brfss/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_eda.ipynb                 # cleaning + EDA
│   ├── 02_statistical_tests.ipynb   # chi² / t / Mann-Whitney
│   └── 03_models.ipynb              # logistic regression + SVM
├── src/
│   ├── preprocess.py                # reusable cleaning helpers
│   ├── stats.py                     # statistical tests
│   └── models.py                    # model pipelines + evaluation
├── reports/
│   └── analysis_writeup.md          # plain-language conclusions
├── figures/                         # export plots here for the README
└── data/
    ├── raw/                         # gitignored — drop CSV locally
    └── processed/                   # gitignored — cleaned tables
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

1. Download the survey CSV you used for the course project into `data/raw/`.
2. Open `notebooks/01_eda.ipynb` and re-run cleaning → EDA → tests → models.
3. Export key plots into `figures/` and paste final metrics into the Results section below.

## Methods (short)

1. **Cleaning** — validate fields, handle missing/corrupted values, standardize the 21 indicators.
2. **EDA** — class balance, univariate distributions, pairwise associations with diabetes.
3. **Inference** — chi-squared for categorical associations; t-test and Mann-Whitney U for group differences.
4. **Modeling** — scaled **logistic regression** and **SVM** baselines with a held-out test set; report discrimination and error modes.

## Results

### Statistical associations
Significant predictors called out in the project analysis:

| Indicator | Why it mattered |
| --- | --- |
| BMI | Strong association with diabetes status |
| Blood pressure | Significant across tests used |
| Cholesterol | Significant across tests used |
| Age | Significant across tests used |

Exact p-values / effect sizes: **TODO — paste from notebooks**.

### Model performance
| Model | Accuracy | Precision | Recall | ROC-AUC |
| --- | --- | --- | --- | --- |
| Logistic regression | TODO | TODO | TODO | TODO |
| SVM | TODO | TODO | TODO | TODO |

> Leave these as TODO until you re-run or copy numbers from the original report — don’t invent metrics.

## My contributions

- Data cleaning and validation on the 70,692-row extract
- Statistical testing across the 21 indicators
- Primary analysis write-up for logistic regression and SVM (methods → results → plain-language conclusions)

Team: **5 members** — TODO: add names/GitHub handles if teammates are OK being listed.

## Stack

Python · Pandas · SciPy · scikit-learn · Matplotlib · Jupyter

## Status / next steps for publishing

- [ ] Drop original notebooks into `notebooks/` (replace the stubs)
- [ ] Fill Results metrics from the real run
- [ ] Add 2–4 figures (class balance, top associations, ROC curves)
- [ ] Confirm exact BRFSS year / source URL
- [ ] Optional: add teammate credits
- [ ] Link this repo from the [portfolio](https://eliu1117-github-io.vercel.app) and profile README

## License

Analysis code: MIT (recommended). Survey data remains under CDC / original dataset terms — not redistributed in this repo.
