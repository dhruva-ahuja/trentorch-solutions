import numpy as np


def solve(X):
    # TODO: Return the Gram matrix X^T X.
    X = np.asarray(X)
    return X.T @ X
