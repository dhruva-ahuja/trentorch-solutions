import numpy as np


def split_heads(x, h):
    """
    x: a sequence of vectors, shape (T, d), with d divisible by h
    h: number of attention heads

    Returns:
        An array of shape (h, T, d // h): each head gets its own slice of the features.
    """
    T, d = x.shape
    return x.reshape(T, h, d // h).transpose(1, 0, 2)
