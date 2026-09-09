# Diabetes Risk Prediction from CDC Health Indicators

Predict diabetes risk from self-reported CDC/BRFSS health indicators using data cleaning, classical statistics, and baseline ML models (logistic regression + SVM).

Built as a **5-person** machine learning project on a balanced **70,692-record** BRFSS 2015 extract with **21** health indicators.

**Live report:** [eliu1117-github-io.vercel.app/projects/diabetes-risk](https://eliu1117-github-io.vercel.app/projects/diabetes-risk)

Also linked from my [portfolio](https://eliu1117-github-io.vercel.app/#projects).

## Highlights

- Cleaned and validated a 70,692-row survey extract in Python / pandas
- Ran chi-squared, two-sample t-tests, and Mann-Whitney U tests on key indicators
- Found **general health, BMI, age, high blood pressure, and high cholesterol** as the strongest predictors
- Trained scaled **logistic regression** and **linear SVM** models (~75% test accuracy)
- Authored the primary analysis write-up for the team report

## Dataset

| Item | Detail |
| --- | --- |
| Source | [CDC BRFSS](https://www.cdc.gov/brfss/annual_data/annual_data.htm) (2015), via the [Kaggle diabetes health indicators extract](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_5050split_health_indicators_BRFSS2015.csv) |
| File used | `diabetes_binary_5050split_health_indicators_BRFSS2015.csv` |
| Rows after cleaning | 70,642 |
| Features | 21 health indicators |
| Target | Diabetes status (binary, 50/50 split) |

> Do not commit the raw CSV. Place it in `data/raw/` locally (gitignored). Survey data remains under CDC / original dataset terms.

## Methods

1. **Cleaning** — reverse intentional “dirtying,” handle missing values, standardize indicators
2. **EDA** — class-conditional distributions across ordinal and binary features
3. **Inference** — chi-squared (high cholesterol), two-sample t-test (BMI), Mann-Whitney U (age)
4. **Modeling** — scaled logistic regression and linear SVM on 14 selected features with an 80/20 holdout

## Results

Full write-up, plots, and code cells live on the [project report page](https://eliu1117-github-io.vercel.app/projects/diabetes-risk).

### Statistical associations

| Test | Indicator | Result |
| --- | --- | --- |
| Chi-squared | High cholesterol | χ² ≈ 5907, p ≈ 0 |
| Two-sample t-test | BMI | t ≈ −81.6, p ≈ 0 |
| Mann-Whitney U | Age group | p ≈ 0 |

Individuals with diabetes tended to have higher BMI and older age groups; high cholesterol was strongly associated with diabetes status.

### Model performance (test set)

| Model | Accuracy | Notes |
| --- | --- | --- |
| Logistic regression | ~75% | Precision / recall ≈ 0.75 for both classes |
| Linear SVM | ~75% | Slightly higher diabetes recall (~0.79) |

Strongest model features in both cases: **general health, BMI, age, high blood pressure, and high cholesterol**.

## Contributions

**Ethan Liu:** data cleaning; primary write-up for exploratory analysis and ML methods/results.

**Team:** Andrew Liu, Ethan Liu, Kaelyn Funchion, Jane Oh, James Lin.

## Stack

Python · pandas · SciPy · scikit-learn · Matplotlib · Jupyter

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

1. Download the Kaggle CSV into `data/raw/`.
2. Open the notebooks under `notebooks/` (or follow the live report) to re-run cleaning → EDA → tests → models.

## License

Analysis code: MIT. Survey data is not redistributed in this repository.
