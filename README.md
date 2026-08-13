# Customer Clustering and XAI Scaffold

This repository is a scaffold for the AI/SW advanced machine learning assignment:
cluster finance customers, train a classifier, and explain predictions with SHAP.

## Structure

- `data_gen.py`: generate `finance_data.csv`.
- `analysis_clustering.py`: run preprocessing, K selection, K-Means, PCA, and persona export.
- `analysis_shap.py`: train/load a scikit-learn classifier and generate SHAP plots.
- `src/data.py`: data loading and feature/target splitting.
- `src/clustering.py`: scaling, Elbow/Silhouette, K-Means, PCA, cluster profiling.
- `src/modeling.py`: classification model training and approval/rejection case selection.
- `src/shap_analysis.py`: TreeExplainer, summary plot, waterfall/force plot, dependence plot.
- `src/reporting.py`: README/report content helpers.
- `outputs/`: generated PNG outputs.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execution Order

```bash
python3 data_gen.py
python3 analysis_clustering.py
python3 analysis_shap.py
```

## Status

Only the requested skeleton is present. Analysis implementations, generated plots, and final business insights still need to be filled in.
