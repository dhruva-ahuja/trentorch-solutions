def has_duplicate(nums):
    """Return True if any value appears at least twice."""
    # This is correct but too slow: it compares every pair of values.
    return len(set(nums)) != len(nums)
