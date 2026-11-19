import numpy as np


def solve(prior, likelihood_h1, likelihood_h0):
    """Implement Bayes Posterior from the mathematical contract in README.md."""

    for val in [prior, likelihood_h0, likelihood_h1]:
        if val > 1 or val < 0:
            raise ValueError()
    
    denom = prior * likelihood_h1 + (1 - prior) * likelihood_h0
    if denom == 0:
        raise ValueError()
    return prior * likelihood_h1 / denom
