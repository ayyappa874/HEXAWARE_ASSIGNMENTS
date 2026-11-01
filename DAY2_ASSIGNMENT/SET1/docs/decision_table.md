# Decision Table - E-Commerce Catalogue and Traffic Analysis (Day 2)

| Problem | Data structure / pattern | Reason (from our own runs) | Complexity |
|---|---|---|---|
| Browse categories in order and look one up | Binary Search Tree | Inorder gives alphabetical order with no extra sort; search took 4 comparisons for 15 categories. Inserting A to Z made it 15 levels, so insert order matters. | O(log n) average, O(n) worst |
| Instant SKU look-up | Hash table with chaining (built-in `dict` in real code) | Direct jump to a bucket: 2.05 us per look-up (dict 0.33 us) against 1,321 us for a list scan. Chaining handles collisions. | O(1) average |
| Deployment order and circular dependency | Directed graph with DFS / BFS | Dependencies are arrows, so a graph fits. DFS names the loop; BFS shows blocked services. Both gave valid orders. | O(V + E) |
| Busiest continuous 3-hour window | Sliding window | Reuses the previous sum (add new, drop old). Same answer as brute force, about 10x faster here. | O(n) |
| Pairs of sorted order values that add up to a gift card | Two pointers | Sorted order shows which pointer to move. About 1,721x faster than checking all pairs on 5,000 values. Needs sorted data. | O(n) |

Timings come from one run on one computer and will differ on yours.
