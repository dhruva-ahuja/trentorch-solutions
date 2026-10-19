# A/B Conversion Rate

Advanced | problemset | data-stats-for-ds | ab-testing

Compute the conversion rate of a control group and a treatment group in an A/B test, and the absolute lift between them. Each group is a list of 0/1 outcomes (1 = the user converted).

Implement `solve(control, treatment)`.

**Returns.** Return a tuple `(control_rate, treatment_rate, lift)` of floats where `lift = treatment_rate - control_rate`. Each group must be a non-empty 1-D sequence of 0/1 values; otherwise `ValueError` is raised.

### Examples

**Example 1**

Input:

```python
solve([0, 1, 0, 0, 1], [1, 1, 0, 1, 1])
```

Output:

```text
(0.4, 0.8, 0.4)
```

**Example 2**

Input:

```python
solve([1, 0, 0, 0], [1, 0, 0, 0])
```

Output:

```text
(0.25, 0.25, 0.0)
```

**Example 3**

Input:

```python
solve([0, 2], [1, 0])
```

Output: Raises `ValueError`.
