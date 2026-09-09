"""Statistical tests used in the diabetes risk analysis."""

from __future__ import annotations

from typing import Iterable

import pandas as pd
from scipy import stats


def chi_square_independence(df: pd.DataFrame, feature: str, target: str = "Diabetes_binary"):
    """Chi-squared test of independence for a categorical feature vs diabetes."""
    table = pd.crosstab(df[feature], df[target])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    return {"feature": feature, "test": "chi2", "stat": chi2, "p": p, "dof": dof}


def two_sample_t(df: pd.DataFrame, feature: str, target: str = "Diabetes_binary"):
    """Two-sample t-test comparing feature means across diabetes classes."""
    a = df.loc[df[target] == 1, feature].dropna()
    b = df.loc[df[target] == 0, feature].dropna()
    stat, p = stats.ttest_ind(a, b, equal_var=False)
    return {"feature": feature, "test": "welch_t", "stat": stat, "p": p}


def mann_whitney_u(df: pd.DataFrame, feature: str, target: str = "Diabetes_binary"):
    """Mann-Whitney U test for a feature across diabetes classes."""
    a = df.loc[df[target] == 1, feature].dropna()
    b = df.loc[df[target] == 0, feature].dropna()
    stat, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    return {"feature": feature, "test": "mannwhitney_u", "stat": stat, "p": p}


def run_indicator_tests(df: pd.DataFrame, features: Iterable[str], target: str = "Diabetes_binary"):
    """Run the project's suite of tests across health indicators."""
    rows = []
    for f in features:
        # Prefer non-parametric + chi-square for survey indicators; keep t-test for continuous-like features.
        rows.append(chi_square_independence(df, f, target))
        rows.append(mann_whitney_u(df, f, target))
        rows.append(two_sample_t(df, f, target))
    return pd.DataFrame(rows)
