# boot-dev-data-structures-and-algorithms

https://www.boot.dev/lessons/f42d132b-ddaa-4461-9b43-26e662e46197

## Ch 2. Math

- logs are inverses of exponents
- `2 ** 4 = 16` => `log2(16) = 4`
- exponents grow rapidly, logs grow slowly - logarithmic algorithms are preferable
- factorials grow faster than exponents

| Input Size | Linear (n\*2) | Quadratic (n^2)      | Log (log2(n)) | n!      |
| ---------- | ------------- | -------------------- | ------------- | ------- |
| 10         | 20 ms         | 100 ms               | 3 ms          | 3628800 |
| 100        | 200 ms        | 10,000 ms            | 7 ms          | ...     |
| 1,000      | 2,000 ms      | 1,000,000 ms         | 10 ms         | ...     |
| 10,000     | 20,000 ms     | 100,000,000 ms       | 14 ms         | ...     |
| 100,000    | 200,000 ms    | 10,000,000,000 ms    | 17 ms         | ...     |
| 1,000,000  | 2,000,000 ms  | 1,000,000,000,000 ms | 20 ms         | ...     |

- exponential decay is the decrease of a value at a rate proportional to its current value

