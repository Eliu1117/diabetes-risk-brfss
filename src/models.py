"""Model training helpers for logistic regression and SVM baselines."""

from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def split_xy(df, feature_cols, target: str = "Diabetes_binary", test_size: float = 0.2, random_state: int = 42):
    X = df[list(feature_cols)]
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


def logistic_pipeline():
    return Pipeline(
        steps=[
            ("scale", StandardScaler()),
            ("clf", LogisticRegression(max_iter=2000)),
        ]
    )


def svm_pipeline(kernel: str = "rbf"):
    return Pipeline(
        steps=[
            ("scale", StandardScaler()),
            ("clf", SVC(kernel=kernel, probability=True)),
        ]
    )


def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    proba = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X_test)[:, 1]
    report = classification_report(y_test, y_pred, digits=3)
    cm = confusion_matrix(y_test, y_pred)
    auc = roc_auc_score(y_test, proba) if proba is not None else None
    return {"report": report, "confusion_matrix": cm, "roc_auc": auc}
