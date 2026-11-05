from collections import defaultdict

def confidence_calibration_bin(
    probs: list[float], labels: list[int], k: int
) -> list[tuple[int, float, float]]:
    """
    probs: predicted probabilities, each in [0, 1].
    labels: binary true labels (0 or 1), same length as probs.
    k: number of equal-width bins.

    bin(p) = min(k - 1, floor(k * p))

    For each of the k bins (in order 0..k-1), return
    (count, mean_prob, positive_rate). For an empty bin, mean_prob and
    positive_rate are both 0.0.
    """
    buckets = defaultdict(list)
    p_rate = defaultdict(list)
    for p, l in zip(probs, labels):
        filled = False
        for b in range(1, k):
            if p < b / k:
                buckets[b].append(p)
                p_rate[b].append(l)
                filled = True
                break
        if filled == False:
            buckets[k].append(p)
            p_rate[k].append(l)

    result = []
    for b in range(1, k+1):
        n = len(buckets[b])
        if n == 0:
            result.append((0, 0, 0))
        else:
            result.append( (n, sum(buckets[b]) / n , sum(p_rate[b]) / n) )
    return result
