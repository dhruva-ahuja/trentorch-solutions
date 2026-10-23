# Directional Derivative

Beginner | problemset | maths-stats-for-ml | calculus

Compute the directional derivative of a scalar function at a point, given the gradient there and a direction. The direction does not need to have length 1.

Implement `solve(grad, direction)`.

**Returns.** Return a float. A zero direction vector has no direction, so the result is `nan`.

### Examples

**Example 1**

Input:

```python
solve([3.0, 4.0], [1.0, 0.0])
```

Output:

```text
3.0
```

**Example 2**

Input:

```python
solve([3.0, 4.0], [3.0, 4.0])
```

Output:

```text
5.0
```
