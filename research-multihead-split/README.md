# Attention Is All You Need: Splitting Into Heads

Beginner | research-papers | transformers | llm | attention | transformer

### The problem, from first principles

Multi-head attention runs several attention functions in parallel, each on a smaller slice of the features. Splitting the vectors into heads is the first step, and it costs no extra parameters.

### From theory to code

Implement `split_heads(x, h)`, which turns a `(T, d)` sequence into `(h, T, d // h)`.

### Constraints

- `d` must be divisible by `h`.

### Hints

<details>
<summary>Hint 1</summary>

Reshape to `(T, h, d // h)`, then transpose so the head axis comes first.

</details>
