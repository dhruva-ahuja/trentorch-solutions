def recommenders_top_k_filter(ids: list[int], scores: list[float], k: int) -> list[int]:
    """
    ids: unique candidate IDs.
    scores: scores[i] is the score for ids[i].
    k: number of top candidates to return.

    Sort by descending score, breaking ties by ascending ID. Return the
    first k IDs in that order.
    """

    return list(map(lambda x: x[1], sorted(list(zip(scores, ids)), key=lambda x: (-x[0], x[1]))))[:k]
