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

- exponential decay is the decrease of a value at a rate proportional to its
  current value
- log scaling is the use of logs to make logarithmic data more easily digestible,
  e.g. by scaling a logarithmic sequence into a linear sequence

## Ch 3. Big-O Analysis

| 5^n | log2(n) |
| --- | ------- |
| 5   | 1       |
| 25  | 2       |
| 125 | 3       |
| 625 | 4       |

- `O(log(n))` is only a little slower than `O(1)` / constant time
- binary search is a `O(log(n))` algorithm

## Ch 4. Sorting algorithms

### Bubble sort

[./ch-04/\_02_bubble_sort.py](./ch-04/_02_bubble_sort.py)

- compare adjacent values in a list, sorting them until we get to the end of
  the list
- Complexity: `O(n^2)`
- Performance:
  - best case, `O(n)` - evaluate each index once, no change
  - worst case, `O(n^2)` - n + (n - 1) + ... + 1 - evaluate every index more
    than once, swap every value

Algorithm:

- set `Swapping` to true
- set `end` to the length of the list
- while `Swapping` is true:
  - set `Swapping` to false
  - for `i` from index 1 to `end`
    - if value at `i - 1` is gt value at `i`, swap positions
    - set `Swapping` to true
  - decrement `end` by 1
- return list

