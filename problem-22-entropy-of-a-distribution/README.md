# Entropy of a Distribution

Advanced | problemset | maths-stats-for-ml | information-theory

Compute the Shannon entropy, in bits, of a discrete probability vector.

Implement `solve(p)`.

**Returns.** Return a float. Entries equal to zero contribute nothing. The input must be a non-empty 1-D vector of non-negative values that sums to 1; otherwise `ValueError` is raised.

### Examples

**Example 1**

Input:

```python
solve([0.5, 0.5])
```

Output:

```text
1.0
```

**Example 2**

Input:

```python
solve([0.25, 0.25, 0.25, 0.25])
```

Output:

```text
2.0
```
