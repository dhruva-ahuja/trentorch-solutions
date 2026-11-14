import numpy as np


def softmax_overflow_incident(logits: np.ndarray) -> np.ndarray:
    """
    logits: array of shape (n, d). Rows are independent.

    Returns an array of shape (n, d): the stable, max-subtracted softmax
    of each row.
    """
    # TODO: subtract each row's max before exponentiating, then
    # normalize each row by its own sum.
    norm_logits = logits - np.max(logits, axis=1, keepdims=True)

    exp_logits = np.exp(norm_logits)

    return exp_logits / np.sum(exp_logits, axis=1, keepdims=True)
