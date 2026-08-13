import importlib

import pytest


def test_required_modules_are_importable():
    for module_name in (
        "data_gen",
        "analysis_clustering",
        "analysis_shap",
        "src.data",
        "src.clustering",
        "src.modeling",
        "src.shap_analysis",
        "src.reporting",
    ):
        importlib.import_module(module_name)


def test_clustering_stubs_fail_explicitly():
    clustering = importlib.import_module("src.clustering")

    with pytest.raises(NotImplementedError):
        clustering.select_optimal_k(None)


def test_shap_stubs_fail_explicitly():
    shap_analysis = importlib.import_module("src.shap_analysis")

    with pytest.raises(NotImplementedError):
        shap_analysis.create_summary_plot(None, None)


def test_reporting_stubs_fail_explicitly():
    reporting = importlib.import_module("src.reporting")

    with pytest.raises(NotImplementedError):
        reporting.build_readme_report({})
