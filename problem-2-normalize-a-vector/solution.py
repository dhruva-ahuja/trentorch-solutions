import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    try:
        x = np.asarray(x)
        if all(x == 0):
            raise Exception()
        return x / np.linalg.norm(x)
    except:
        raise ValueError()
        return 0
