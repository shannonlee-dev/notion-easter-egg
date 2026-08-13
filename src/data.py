"""Data loading and preprocessing boundaries for the finance XAI mission."""

from __future__ import annotations

from typing import Any


TARGET_COLUMNS = ("credit_score", "is_overdue")


def load_finance_data(path: str = "finance_data.csv") -> Any:
    """Load the Mission 23 finance CSV."""
    raise NotImplementedError("Load finance_data.csv with pandas.")


def split_features_targets(dataframe: Any) -> tuple[Any, Any, Any]:
    """Split features from `credit_score` and `is_overdue` target columns."""
    raise NotImplementedError("Exclude target columns from clustering features.")


def preprocess_features(features: Any) -> Any:
    """Handle missing values/outliers and scale features for distance-based clustering."""
    raise NotImplementedError("Apply allowed preprocessing and scaling.")
