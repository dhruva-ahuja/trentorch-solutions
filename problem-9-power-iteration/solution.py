import numpy as np


def solve(A, steps=100):
    A = np.asarray(A)
    m, n = A.shape

    if m != n:
        raise ValueError(f"Given matrix is not square matrix, dimensions {m}x{n}")

    v = np.ones(m)
    v_norm = v / np.linalg.norm(v)

    for _ in range(steps):
        v = A @ v_norm
        if np.all(v == 0):
            return v.flatten()
        v_norm = v / np.linalg.norm(v)

    return v_norm.flatten()
