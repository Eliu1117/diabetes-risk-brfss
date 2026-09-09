# Analysis write-up (draft skeleton)

> Ethan authored the primary analysis write-up for logistic regression and SVM for the team report.
> Paste or link the final collaborative write-up here (or keep a PDF in `reports/`).

## Question
Can self-reported CDC/BRFSS health indicators predict diabetes risk, and which indicators are most associated with diabetes status?

## Data
- Source: CDC Behavioral Risk Factor Surveillance System (BRFSS) health indicators
- Working sample after cleaning: **70,692** records
- Features: **21** health indicators (+ diabetes label)
- Team size: **5**

## Cleaning
- TODO: summarize corrupted-feature fixes and missing-value handling

## Statistical findings
Indicators flagged as significant predictors in the project analysis:
- BMI
- Blood pressure
- Cholesterol
- Age

Tests used: chi-squared, two-sample t-test, Mann-Whitney U.

## Models
| Model | Key metrics (fill in) |
| --- | --- |
| Logistic regression | accuracy / precision / recall / ROC-AUC: **TODO** |
| Support vector machine | accuracy / precision / recall / ROC-AUC: **TODO** |

## Conclusions
- TODO: 3–5 sentences translating model results into plain-language statistical conclusions
