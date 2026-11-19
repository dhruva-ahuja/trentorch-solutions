import numpy as np

def solve(logits):
    try:
        logits_new = logits - np.max(logits)
        exp_logits = np.exp(logits_new)
        return exp_logits / np.sum(exp_logits)
    except Exception as e:
        raise e
