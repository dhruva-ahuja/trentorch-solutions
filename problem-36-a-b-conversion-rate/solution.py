import numpy as np


def solve(control, treatment):
    """Implement A/B Conversion Rate from the mathematical contract in README.md."""
    if isinstance(control, int):
        control = [control]
    if isinstance(treatment, int):
        treatment = [treatment]
    if len(control) < 1 or len(treatment) < 1:
        raise ValueError("Length should not be zero")
    if not all(x == 0 or x == 1 for x in control) or not all(x == 0 or x == 1 for x in treatment):
        raise ValueError("Values not 0 or 1")
    c_r = sum(control) / len(control)
    t_r = sum(treatment) / len(treatment)

    return c_r, t_r, t_r - c_r
