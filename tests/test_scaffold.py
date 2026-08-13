import importlib

import pytest


def test_required_modules_are_importable():
    for module_name in ("src.linear_algebra", "src.calculus", "src.optimizer"):
        importlib.import_module(module_name)


def test_linear_algebra_stubs_fail_explicitly():
    linear_algebra = importlib.import_module("src.linear_algebra")

    with pytest.raises(NotImplementedError):
        linear_algebra.create_unit_circle()


def test_calculus_stubs_fail_explicitly():
    calculus = importlib.import_module("src.calculus")

    with pytest.raises(NotImplementedError):
        calculus.numerical_derivative(lambda x: x**2, x=3.0)


def test_optimizer_stubs_fail_explicitly():
    optimizer = importlib.import_module("src.optimizer")
    gd = optimizer.VanillaGD(learning_rate=0.1)

    with pytest.raises(NotImplementedError):
        gd.step([1.0, 1.0], [2.0, 2.0])
