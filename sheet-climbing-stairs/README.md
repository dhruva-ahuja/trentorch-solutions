# Climbing Stairs

Beginner | dsa-sheet | dynamic-programming | sequences-and-counting

You climb a staircase with `n` steps. Each move goes up **1 or 2** steps. Return the **number of different ways** to reach the top, modulo `10**9 + 7`.

For `n = 3` the answer is `3` (`1+1+1`, `1+2`, `2+1`).

The starter code is a plain recursion. It is correct but far too slow for large `n`.

### Examples

**Example 1**

Input:

```python
climb_stairs(3)
```

Output:

```text
3
```

**Example 2**

Input:

```python
climb_stairs(5)
```

Output:

```text
8
```

### Constraints

- `0 <= n <= 1000000`
