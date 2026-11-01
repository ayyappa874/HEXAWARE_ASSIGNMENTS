# Final Takeaways (in simple words)

1. **Task 1 - Search:** If data is sorted, use binary search. It cuts the work in half every step, so 50,000 records need only ~16 checks instead of 50,000. Sorting first costs time, so it pays off when you search many times.
2. **Task 2 - Sorting:** Two nested loops (bubble sort) become painfully slow as data grows - 10,000 records took about 7.9 seconds, merge sort took 0.035 seconds. In real projects just use the built-in `sorted()`; know the slow ones to understand *why*.
3. **Task 3 - Duplicates by sorting:** Sorting is a powerful trick: it puts look-alike items next to each other, so finding duplicates becomes a simple "compare with the neighbour" loop. The key is choosing the right sort key - (customer, amount, minute). Cost: O(n log n) time, O(n) space. (Hashing would be O(n) on average but needs a hash table; sorting needs no hashing and gives ordered results.)
4. **Task 4 - Stack & Queue:** Pick the structure that matches the behaviour. "Undo" = last in, first out -> Stack. "Waiting line" = first in, first out -> Queue. Python's built-in `list` and `deque` are faster than hand-built versions, and never use `list.pop(0)` as a queue.
5. **Task 5 - Greedy vs DP:** Greedy (take the biggest coin) is quick and works for normal currency, but it can be wrong for odd coin sets (coins 1,3,4 for 6). DP checks every possibility and is always right. Rule: **if you cannot prove greedy works, use DP.**

**Big picture:** the right algorithm and data structure matter more than faster hardware. Always (1) understand the data, (2) pick the structure that fits, (3) measure, and (4) verify with tests.
