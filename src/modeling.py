"""Classification model scaffold for overdue prediction."""

from __future__ import annotations

from typing import Any


def train_overdue_classifier(features: Any, target: Any, random_state: int = 42) -> Any:
    """Train a scikit-learn tree-based classifier such as RandomForestClassifier."""
    raise NotImplementedError("Train classifier using scikit-learn built-in models only.")


def predict_overdue_probabilities(model: Any, features: Any) -> Any:
    """Return predicted probability for `is_overdue=1`."""
    raise NotImplementedError("Return positive-class probabilities.")


def select_local_cases(dataframe: Any, probabilities: Any) -> dict[str, Any]:
    """Select one rejection case and one approval case for Local SHAP explanation."""
    raise NotImplementedError("Select high-risk rejection and low-risk approval examples.")


def select_cluster_representatives(dataframe: Any, labels: Any, probabilities: Any) -> Any:
    """Select representative customers per cluster for persona-linked explanations."""
    raise NotImplementedError("Pick representative customer rows by cluster.")
