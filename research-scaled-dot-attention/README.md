# Attention Is All You Need: Scaled Dot-Product Attention

Intermediate | research-papers | transformers | llm | attention | transformer

### The problem, from first principles

Attention Is All You Need (Vaswani et al., 2017) drops recurrence entirely. Each position builds its output by comparing a query with every key, turning the similarities into weights, and averaging the values with those weights. Dividing by the square root of the key dimension keeps the softmax from saturating.

### From theory to code

Implement `scaled_dot_product_attention(Q, K, V)`, which returns `softmax(Q K^T / sqrt(d)) V` with a row-wise softmax.

### Constraints

- `Q` and `K` share the feature dimension `d`.

### Hints

<details>
<summary>Hint 1</summary>

Compute `Q @ K.T / sqrt(d)`, apply a row-wise softmax with the max-subtraction trick, then multiply by `V`.

</details>
