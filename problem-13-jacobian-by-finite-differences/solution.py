import numpy as np


# def solve(f, x, h=1e-5):
#     x = np.asarray(x, float)
#     y = np.asarray(f(x), float)
#     J = np.zeros((len(y), len(x)))
#     for j in range(len(x)):
#         e = np.zeros_like(x)
#         e[j] = h
#         J[:, j] = (np.asarray(f(x + e)) - np.asarray(f(x - e))) / (2 * h)
#     return J


def solve(f, x, h=1e-05):
    """Implement Jacobian by Finite Differences from the mathematical contract in README.md."""
    try:
        x = np.asarray(x, dtype=float)
        n = x.shape[0]
        y = f(x)
        result = []
        for i in range(n):
            dx = np.zeros_like(x)
            dx[i] = h
    
            xhp = x + dx
            xhn = x - dx
    
            fxhp = f(xhp)
            fxhn = f(xhn)
    
            fi = (fxhp - fxhn) / (2*h)
    
            result.append(fi)
    
        result = np.asarray(result).T
        return result
    except Exception as e:
        raise e
