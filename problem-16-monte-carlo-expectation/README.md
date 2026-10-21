# Monte Carlo Expectation

Beginner | problemset | maths-stats-for-ml | probability

Estimate the expectation $\mathbb E[f(X)]$ from samples of $X$ by averaging $f$ over the samples.

Implement `solve(f, samples)`.

**Returns.** Return a float. An empty sample gives `nan`.

### Examples

**Example 1**

Input:

```python
solve(lambda s: s**2, [1.0, 2.0, 3.0])
```

Output:

```text
4.666667
```

**Example 2**

Input:

```python
solve(lambda s: s, [0.0, 10.0])
```

Output:

```text
5.0
```
