import numpy as np


def solve(f, x, h=1e-05):
    """Implement Finite Difference Derivative from the mathematical contract in README.md."""

    try:
        y_f = f(x + h)
        y_b = f(x - h)

        return (y_f - y_b) / (2 * h)

    except Exception as e:
        raise e
