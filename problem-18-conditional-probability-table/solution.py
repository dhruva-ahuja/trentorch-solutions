import numpy as np


def solve(A, B):
    A, B = np.asarray(A), np.asarray(B)
    if A.size == 0 or B.size == 0:
        return 0
    if np.all(A == 0) or np.all(B == 0):
        return 0
    A = A != 0
    B = B != 0
    return (A & B).sum() / B.sum()
