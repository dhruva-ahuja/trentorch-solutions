# Bayes Posterior

Intermediate | problemset | maths-stats-for-ml | bayesian-inference

Compute the posterior probability of hypothesis $H_1$ from its prior probability and the likelihood of the observed evidence under $H_1$ and under $H_0$.

Implement `solve(prior, likelihood_h1, likelihood_h0)`.

**Returns.** Return a float in $[0, 1]$. The prior of $H_0$ is $1-\text{prior}$. The prior and both likelihoods must lie in $[0, 1]$, and if the total evidence $P(e)$ is zero the posterior does not exist; both cases raise `ValueError`.

### Examples

**Example 1**

Input:

```python
solve(0.5, 0.8, 0.2)
```

Output:

```text
0.8
```

**Example 2**

Input:

```python
solve(0.01, 0.9, 0.05)
```

Output:

```text
0.153846
```
