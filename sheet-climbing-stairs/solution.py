def climb_stairs(n: int) -> int:
    """Return the number of ways to climb n stairs, modulo 10**9 + 7."""
    # This is correct but too slow: it solves the same smaller problems again and again.
    a, b = 1, 1

    for i in range(2, n+1):
        b, a = (b + a) % (10**9 + 7), b

    return b
    # return (climb_stairs(n - 1) + climb_stairs(n - 2)) % (10**9 + 7)
