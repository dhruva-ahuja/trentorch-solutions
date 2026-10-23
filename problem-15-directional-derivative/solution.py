import numpy as np


def solve(grad, direction):
    """Implement Directional Derivative from the mathematical contract in README.md."""
    grad = np.asarray(grad)
    direction = np.asarray(direction)

    return grad @ direction / np.linalg.norm(direction)
