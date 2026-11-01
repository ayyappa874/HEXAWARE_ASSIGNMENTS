# One-Page Note - Complexity & Data-Structure Rationale
**Retail Order Desk | Day 1 - Problem Solving Techniques & Data Structures I**

| # | Task | Technique / Structure | Time | Extra Space | Why this choice |
|---|---|---|---|---|---|
| 1 | Find an order by ID | **Linear search** | O(n) | O(1) | Works on unsorted data; fine for one-off lookups |
| 1 | | **Binary search** | O(log n) | O(1) | Order IDs are already sorted, so halving the range is ~400x faster on 50,000 records |
| 2 | Rank by amount | **Bubble sort** | O(n^2) | O(1) | Simple to trace; shows why quadratic sorting does not scale (about 7.9 s for 10,000) |
| 2 | | **Merge sort** | O(n log n) | O(n) | Predictable speed, stable; 0.035 s for 10,000 |
| 2 | | Built-in `sorted()` | O(n log n) | O(n) | Fastest in practice (C-optimised Timsort); use in production |
| 3 | Duplicate orders | **Sorting + adjacent scan** (no hashing) | O(n log n) | O(n) | Equal (customer, amount, minute) keys become neighbours, so one pass finds every group; no hash table needed and output is ordered |
| 4 | Undo last edit | **Stack** (linked list) | O(1) push/pop | O(n) stored | Undo needs the most recent action first = LIFO |
| 4 | Dispatch line | **Queue** (linked list, head+tail) | O(1) enqueue/dequeue | O(n) stored | Fair service needs the oldest order first = FIFO; tail pointer makes enqueue O(1) |
| 4 | | Built-ins `list` / `deque` | O(1) | O(n) | ~10x faster than hand-made classes; `list.pop(0)` is O(n) and slow |
| 5 | Min notes/coins | **Greedy** | O(k) | O(1) | Optimal for Indian currency (verified for 1..3000); very fast |
| 5 | | **Dynamic programming** | O(amount x k) | O(amount) | Needed when greedy fails, e.g. coins [1,3,4], refund 6: greedy = 3 coins, DP = 2 |

(n = number of orders, k = number of denominations)

**Measured on this run (50,000 / 10,000 records):** binary search ~396x faster than linear; merge sort ~226x faster than bubble sort; built-in list/deque ~10x faster than custom Stack/Queue; `list.pop(0)` queue ~3.3 s for 50,000 items.
*Timings vary by computer; the Big-O ordering never changes.*
