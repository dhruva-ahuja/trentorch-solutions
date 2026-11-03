import numpy as np
import math


def solve(A):
    # TODO: Return the Frobenius norm of A.
    A = np.asarray(A)
    return math.sqrt(np.sum(A*A))
