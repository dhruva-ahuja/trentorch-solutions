import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    a = np.asarray(a)
    b = np.asarray(b)

    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))
