# AI Math Learning Scaffold

This repository is a scaffold for the AI/SW advanced AI math assignment.

## Structure

- `src/linear_algebra.py`: matrix transforms, power iteration, determinant-area checks, and SVD image compression.
- `src/calculus.py`: numerical differentiation and gradient visualization.
- `src/optimizer.py`: Vanilla GD, Momentum, and convergence path visualization.
- `notebooks/backprop_derivation.ipynb`: two-layer neural network forward/backward derivation notes.
- `notebooks/probability_loss.ipynb`: probability distributions and MLE-loss derivation notes.
- `outputs/`: generated PNG outputs.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verification

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest
python3 -B -c "import ast, pathlib; [ast.parse(p.read_text()) for p in pathlib.Path('src').glob('*.py')]"
```

## Status

Only the module and notebook skeletons are present. Mathematical implementations, derivations, and generated plots still need to be filled in.
