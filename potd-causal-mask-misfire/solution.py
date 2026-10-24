import numpy as np
from scipy.special import softmax

def causal_mask_misfire(scores: np.ndarray) -> np.ndarray:
    """
    Row-wise, numerically stable softmax under a causal mask: for query
    row i, only key columns j <= i are visible. Forbidden entries (j > i)
    must be exactly 0.0 in the output.

    scores: shape (n, n).
    """
    m, n = scores.shape

    for i in range(m):
        for j in range(i+1, n):
            scores[i, j] = -np.inf

    
    # TODO: mask with -inf BEFORE taking the row max, so forbidden entries
    # never influence the max-subtraction or the normalizer.
    return np.apply_along_axis(softmax, axis=1, arr=scores)
