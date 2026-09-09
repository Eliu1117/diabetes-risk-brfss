"""Data cleaning helpers for the CDC/BRFSS diabetes indicators dataset.

TODO: move reusable cleaning steps out of notebooks into functions here.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_raw(path: str | Path) -> pd.DataFrame:
    """Load the raw survey CSV."""
    return pd.read_csv(path)


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder cleaning pipeline — replace with the project's real steps.

    Expected work from the project write-up:
    - drop / impute missing values
    - resolve corrupted feature values
    - standardize dtypes for the 21 health indicators
    """
    out = df.copy()
    # TODO: implement project-specific cleaning
    return out
