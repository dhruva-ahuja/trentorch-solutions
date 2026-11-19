# Jacobian by Finite Differences

Beginner | problemset | maths-stats-for-ml | calculus

Estimate the Jacobian of a vector-valued function $f:\mathbb R^n\to\mathbb R^m$ at a point, one column at a time, with centered finite differences.

Implement `solve(f, x, h=1e-5)`.

**Returns.** Return an $m\times n$ NumPy array whose entry $(i, j)$ approximates $\partial f_i/\partial x_j$.

### Examples

**Example 1**

Input:

```python
solve(lambda z: np.array([z[0]**2, z[0]*z[1]]), [1.0, 2.0])
```

Output:

```text
[[2.0, 0.0], [2.0, 1.0]]
```

**Example 2**

Input:

```python
solve(lambda z: np.array([np.sin(z[0])]), [0.0])
```

Output:

```text
[[1.0]]
```
