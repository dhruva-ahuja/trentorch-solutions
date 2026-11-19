# Finite Difference Derivative

Advanced | problemset | maths-stats-for-ml | calculus

Estimate the derivative $f'(x)$ of a scalar function at a point with a centered finite difference and step `h`.

Implement `solve(f, x, h=1e-5)`.

**Returns.** Return a float.

### Examples

**Example 1**

Input:

```python
solve(lambda t: t**2, 3.0)
```

Output:

```text
6.0
```

**Example 2**

Input:

```python
solve(lambda t: t**3, 2.0)
```

Output:

```text
12.0
```
