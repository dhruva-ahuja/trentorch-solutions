# Bernoulli Mean and Variance

Intermediate | problemset | maths-stats-for-ml | probability

Compute the empirical mean and variance of binary (0/1) observations.

Implement `solve(x)`.

**Returns.** Return a tuple `(mean, variance)` of floats, where the variance is $\hat p(1-\hat p)$. Empty input, non-binary values or a non-1-D input raise `ValueError`.

### Examples

**Example 1**

Input:

```python
solve([1, 0, 1, 1])
```

Output:

```text
(0.75, 0.1875)
```

**Example 2**

Input:

```python
solve([0, 0, 0])
```

Output:

```text
(0.0, 0.0)
```
