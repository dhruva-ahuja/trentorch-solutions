# Conditional Probability Table

Intermediate | problemset | maths-stats-for-ml | probability

Estimate $P(A\mid B)$ from paired binary observations: among the cases where $B$ happened, the fraction where $A$ also happened.

Implement `solve(A, B)`.

**Returns.** Return a float. Any non-zero entry counts as true. If $B$ never occurs the conditional probability is undefined and the function returns `0.0`.

### Examples

**Example 1**

Input:

```python
solve([1, 0, 1, 1], [1, 1, 1, 0])
```

Output:

```text
0.666667
```

**Example 2**

Input:

```python
solve([1, 1], [0, 0])
```

Output:

```text
0.0
```
