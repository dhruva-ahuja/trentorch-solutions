# distance-normalized-features: Uber case

Beginner | problemset | maths-stats-for-ml | linear-algebra | uber

The team needs a reliable implementation for embedding preprocessing in a production-oriented ML workflow. A small implementation error can change the model input or metric enough to make a downstream result misleading.

Normalize each numeric feature vector to unit L2 norm before it enters a similarity model.

Scale the vector so its Euclidean (L2) length is exactly 1 while its direction stays the same. The all-zero vector has no direction, so it is returned unchanged.

Implement `solve(x)`.

**Returns.** Return a float NumPy vector of the same shape.

### Examples

**Example 1**

Input:

```python
solve([3.0, 4.0])
```

Output:

```text
[0.6, 0.8]
```

**Example 2**

Input:

```python
solve([0.0, 0.0])
```

Output:

```text
[0.0, 0.0]
```
