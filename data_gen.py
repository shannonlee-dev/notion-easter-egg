"""Generate the finance dataset used by the clustering and XAI mission."""

from __future__ import annotations


def generate_finance_data(output_path: str = "finance_data.csv", n_samples: int = 10_000, random_state: int = 42) -> None:
    """Generate `finance_data.csv` with customer features and target columns."""
    raise NotImplementedError("Create the Mission 23 finance dataset with pandas and NumPy.")


def main() -> None:
    """CLI entry point for dataset generation."""
    generate_finance_data()


if __name__ == "__main__":
    main()
