import numpy as np

def solve(coeffs):
    """Solve the system a*x + b*y = e and c*x + d*y = f, where coeffs is [a,b,c,d,e,f]. A singular system raises ValueError."""
    a, b, c, d, e, f = coeffs
    if a*d - b*c == 0:
        raise ValueError()
    inv = np.linalg.inv([[a, b], [c, d]])
    return (inv @ np.array([e, f]).reshape(-1, 1)).flatten()
