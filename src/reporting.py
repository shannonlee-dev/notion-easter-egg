"""README/report helper scaffold for business-facing XAI insights."""

from __future__ import annotations

from typing import Any


def build_cluster_summary_table(cluster_summary: Any, personas: dict[int, str]) -> str:
    """Build a Markdown table summarizing cluster statistics and personas."""
    raise NotImplementedError("Format cluster summary table.")


def build_global_shap_section(feature_importance: Any) -> str:
    """Build the Global SHAP interpretation section."""
    raise NotImplementedError("Describe top features, direction, and business meaning.")


def build_local_case_section(local_cases: dict[str, Any]) -> str:
    """Build the approval/rejection Local SHAP case section."""
    raise NotImplementedError("Explain selected customers and prediction reasons.")


def build_action_recommendations(personas: dict[int, str]) -> str:
    """Build cluster-specific marketing and risk-management recommendations."""
    raise NotImplementedError("Write target/message/action recommendations.")


def build_readme_report(analysis_context: dict[str, Any]) -> str:
    """Assemble the final README report from analysis artifacts."""
    raise NotImplementedError("Generate the business insight report content.")
