import numpy as np


def attention_firewall(
    q: np.ndarray, keys: np.ndarray, values: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    q: array of shape (d,), the query for the final position.
    keys: array of shape (n, d).
    values: array of shape (n, dv).

    s_j = (q . keys[j]) / sqrt(d)
    p = softmax(s) (numerically stable, max-subtracted)
    o = sum_j p_j * values[j]

    Returns (p, o): the attention probabilities (shape (n,)) and the
    output vector (shape (dv,)).
    """
    d = q.shape[0]
    s = (keys @ q) / np.sqrt(d)

    def softmax(x):
        x_exp = np.exp(x - np.max(x))
        return x_exp / np.sum(x_exp)

    p = softmax(s)
    o = values.T @ p

    return (p, o)
