import numpy as np


def solve(x):
    """Implement Bernoulli Mean and Variance from the mathematical contract in README.md."""
    x = np.asarray(x)
    if x.size == 0 or x.ndim > 1:
        raise ValueError()
    if not np.all((x == 1) | (x == 0)):
        raise ValueError()
    
    p = x.mean()

    return p, p*(1-p)
