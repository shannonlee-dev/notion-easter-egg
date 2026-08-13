"""Run customer clustering analysis from `finance_data.csv`."""

from __future__ import annotations


def run_clustering_analysis(data_path: str = "finance_data.csv", output_dir: str = "outputs") -> None:
    """Run preprocessing, K selection, K-Means, PCA visualization, and persona profiling."""
    raise NotImplementedError("Wire clustering pipeline steps and save output figures/tables.")


def main() -> None:
    """CLI entry point for clustering analysis."""
    run_clustering_analysis()


if __name__ == "__main__":
    main()
