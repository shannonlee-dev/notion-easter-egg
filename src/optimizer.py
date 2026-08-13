"""Optimization utilities for the AI math assignment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class VanillaGD:
    """Vanilla gradient descent optimizer."""

    learning_rate: float

    def step(self, params: Any, gradient: Any) -> Any:
        """Return one gradient descent update."""
        raise NotImplementedError("Implement vanilla gradient descent update.")

    def optimize(self, initial_point: Any, gradient_function: Callable[[Any], Any], num_steps: int = 100) -> list[Any]:
        """Run gradient descent and return the full optimization path."""
        raise NotImplementedError("Collect parameter path across iterations.")


@dataclass
class Momentum:
    """Momentum gradient descent optimizer."""

    learning_rate: float
    beta: float = 0.9
    velocity: Any = field(default=None)

    def step(self, params: Any, gradient: Any) -> Any:
        """Return one momentum gradient descent update."""
        raise NotImplementedError("Implement momentum gradient descent update.")

    def optimize(self, initial_point: Any, gradient_function: Callable[[Any], Any], num_steps: int = 100) -> list[Any]:
        """Run momentum optimization and return the full optimization path."""
        raise NotImplementedError("Collect momentum path across iterations.")


def circular_quadratic(point: Any) -> float:
    """Return f(x,y)=x^2+y^2."""
    raise NotImplementedError("Evaluate circular quadratic function.")


def circular_quadratic_gradient(point: Any) -> Any:
    """Return the gradient of f(x,y)=x^2+y^2."""
    raise NotImplementedError("Return [2x, 2y].")


def elliptical_quadratic(point: Any) -> float:
    """Return f(x,y)=x^2+10y^2."""
    raise NotImplementedError("Evaluate elliptical quadratic function.")


def elliptical_quadratic_gradient(point: Any) -> Any:
    """Return the gradient of f(x,y)=x^2+10y^2."""
    raise NotImplementedError("Return [2x, 20y].")


def plot_convergence_paths(paths: dict[str, list[Any]], function: Callable[[Any], float], output_path: str | None = None) -> Any:
    """Plot optimizer paths over a contour map."""
    raise NotImplementedError("Render dotted convergence paths on contours.")


def compare_optimizers(output_path: str | None = None) -> Any:
    """Compare VanillaGD and Momentum on circular and elliptical quadratic functions."""
    raise NotImplementedError("Generate optimizer comparison figures.")
