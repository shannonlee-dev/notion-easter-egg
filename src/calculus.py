"""Calculus utilities for the AI math assignment."""

from __future__ import annotations

from typing import Any, Callable


def numerical_derivative(function: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    """Estimate f'(x) with the central difference formula."""
    raise NotImplementedError("Implement central-difference numerical derivative.")


def validate_square_derivative(x: float = 3.0) -> dict[str, float]:
    """Compare the numerical derivative of f(x)=x^2 at x=3 with the analytic value 6."""
    raise NotImplementedError("Check absolute error is within 1e-4.")


def gradient_2d(function: Callable[[float, float], float], x: float, y: float, h: float = 1e-5) -> tuple[float, float]:
    """Estimate the 2D gradient vector with central differences."""
    raise NotImplementedError("Compute partial derivatives with central differences.")


def quadratic_function(x: Any, y: Any) -> Any:
    """Return f(x, y)=x^2+y^2 for contour and gradient experiments."""
    raise NotImplementedError("Evaluate the 2D quadratic test function.")


def plot_gradient_field(output_path: str | None = None) -> Any:
    """Plot contours of f(x,y)=x^2+y^2 and overlay gradient arrows."""
    raise NotImplementedError("Visualize gradient vectors perpendicular to contours.")
