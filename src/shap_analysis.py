"""SHAP interpretation scaffold for global and local model explanations."""

from __future__ import annotations

from typing import Any


def build_tree_explainer(model: Any, background_data: Any | None = None) -> Any:
    """Create a SHAP TreeExplainer for a tree-based scikit-learn model."""
    raise NotImplementedError("Use shap.TreeExplainer as the primary explainer.")


def compute_shap_values(explainer: Any, features: Any) -> Any:
    """Compute SHAP values for model interpretation."""
    raise NotImplementedError("Compute SHAP values, sampling if needed for runtime.")


def create_summary_plot(shap_values: Any, features: Any, output_path: str = "outputs/shap_summary.png") -> None:
    """Save a SHAP Summary Plot showing global feature importance and direction."""
    raise NotImplementedError("Save SHAP summary plot as PNG.")


def create_waterfall_plot(explainer: Any, shap_values: Any, row_index: int, output_path: str) -> None:
    """Save a local SHAP Waterfall Plot for a selected customer."""
    raise NotImplementedError("Save local explanation plot as PNG.")


def create_force_plot_html(explainer: Any, shap_values: Any, row_index: int, output_path: str) -> None:
    """Save a local SHAP Force Plot as HTML when waterfall output is not suitable."""
    raise NotImplementedError("Save force plot HTML with shap.initjs when needed.")


def create_dependence_plot(shap_values: Any, features: Any, feature_name: str, output_path: str) -> None:
    """Save a SHAP Dependence Plot for one selected feature."""
    raise NotImplementedError("Save dependence plot PNG and support top/business features.")


def choose_dependence_features(summary_importance: Any) -> list[str]:
    """Choose 1-2 top SHAP features plus one business-meaningful feature."""
    raise NotImplementedError("Select dependence plot features.")
