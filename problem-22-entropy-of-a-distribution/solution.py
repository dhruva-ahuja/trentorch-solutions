import numpy as np


def solve(p):
    # TODO: Return the Shannon entropy (base 2) of the positive entries of p.
    result = 0
    try:
        if sum(p) != 1:
            raise ValueError()
    except:
        raise ValueError()
    for val in p:
        if val > 0:
            result -= val * np.log2(val)
        elif val == 0:
            continue
        else:
            raise ValueError()

    return result
