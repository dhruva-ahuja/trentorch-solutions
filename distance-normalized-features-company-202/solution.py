import numpy as np

def solve(x):
    """Implement distance-normalized-features from the mathematical contract in README.md."""
    norm = np.linalg.norm(x)
    if norm == 0:
        return x
    else:
        return x / norm
