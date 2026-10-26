import numpy as np

def gradient_accumulator(
    theta: float, eta: float, microbatches: list[tuple[int, float]]
) -> tuple[float, float]:
    """
    microbatches: list of (n_j, g_j) pairs, n_j examples with mean
    gradient g_j.

    g = sum(n_j * g_j) / sum(n_j)   (example-weighted mean, NOT the mean
    of the microbatch means).
    theta' = theta - eta * g.

    Return (g, theta_prime).
    """
    # TODO: weight by example count, divide exactly once.
    n_j, g_j = zip(*microbatches)
    n_j, g_j = np.asarray(n_j), np.asarray(g_j)
    g = np.sum(n_j * g_j) / np.sum(n_j)

    return g, theta - eta * g
