import numpy as np


def scaled_dot_product_attention(Q, K, V):
    """
    Q: queries, shape (T_q, d)
    K: keys, shape (T_k, d)
    V: values, shape (T_k, d_v)

    Returns:
        softmax(Q K^T / sqrt(d)) V, shape (T_q, d_v).
    """
    # TODO: Compute the scaled scores, take a row-wise softmax, and weight the values (see Theory).
    Q, K, V = [np.asarray(_) for _ in [Q, K, V]]
    T_q, d = Q.shape
    T_k, d_v = V.shape

    logits = Q @ K.T / np.sqrt(d)
    norm_logits = logits - np.max(logits)
    exp_logits = np.exp(norm_logits)
    dist = exp_logits / np.sum(exp_logits) @ V
    return dist
