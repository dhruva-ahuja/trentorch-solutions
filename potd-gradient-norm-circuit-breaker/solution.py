import numpy as np


def gradient_norm_circuit_breaker(g: np.ndarray, c: float) -> tuple[float, np.ndarray]:
    """
    g: array of shape (n,), the gradient vector.
    c: clipping threshold, c > 0.

    Returns (norm, g_tilde): the original L2 norm of g, and the
    globally rescaled vector (unchanged if norm <= c, otherwise scaled
    by c / norm so every component shrinks by the same factor).
    """
    g2_norm = np.linalg.norm(g)

    if g2_norm > c:
        g = g * c / g2_norm
    return g2_norm, g
