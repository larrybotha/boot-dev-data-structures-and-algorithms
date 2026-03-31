# boot-dev-data-structures-and-algorithms

[https://www.boot.dev/lessons/f42d132b-ddaa-4461-9b43-26e662e46197](https://www.boot.dev/lessons/f42d132b-ddaa-4461-9b43-26e662e46197)

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

### Merge sort

- comprised of 2 functions:\
  - `merge_sort`: function that splits array into halves
  - `merge`: function that takes 2 sorted arrays and merges them
- Complexity: `O(n log(n))`
- merge sort is _stable_ - i.e. duplicate values in the original list will be in
  the same order in the resulting list
- does not perform well on small arrays due to the memory overhead of splitting
  arrays into smaller and smaller arrays
- recursion can come at a cost penalty in languages that don't support tail-recursion,
  such as Python

Algorithm:

- `merge_sort(xs: list) -> list`
  - if `len(xs) < 2`, already sorted
  - split `xs` into two arrays down the middle
  - call itself with each array
  - return the result of calling `merge` on the two halves
- `merge(xs: list, ys: list) -> list`
  - create `zs` - the final array to return
  - set `i` and `j` to 0
  - loop over `xs` and `ys`, comparing values
    - if `x < y`, add `x` to `zs`, increment `i`
    - else, add `y` to `zs`, incremen `j`
    - continue until either list is exhausted
  - if remaining items from `xs` or `ys`, append to `zs`
  - return `zs`
