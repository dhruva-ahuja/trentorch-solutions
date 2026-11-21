from typing import Tuple
import math

def training_step_estimator(n: int, b: int, e: int) -> Tuple[int, int]:
    """
    n: number of examples.
    b: batch size.
    e: number of epochs.

    Steps per epoch retains the final partial batch, so it is the integer
    ceiling of n / b (computed with exact integer arithmetic, not
    floating-point division). Total steps = e * steps_per_epoch. Return
    (steps_per_epoch, total_steps).
    """
    # TODO: compute ceil(n / b) via integer arithmetic, then multiply by e.
    mul = int(math.ceil(n / b))
    return mul, mul * e
