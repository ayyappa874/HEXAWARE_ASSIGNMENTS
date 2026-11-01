# Dry Runs (hand-traced on the 20-record dataset)

A dry run = executing the algorithm on paper, step by step, tracking every variable.

---

## Task 1 - Binary search for orderId = 1014 (20 sorted records, positions 0-19)

Position of 1001 is 0, so 1014 is at position 13.

| Step | low | high | mid | orders[mid].orderId | Compare with 1014 | Action |
|---|---|---|---|---|---|---|
| 1 | 0  | 19 | 9  | 1010 | 1010 < 1014 | low = 10 |
| 2 | 10 | 19 | 14 | 1015 | 1015 > 1014 | high = 13 |
| 3 | 10 | 13 | 11 | 1012 | 1012 < 1014 | low = 12 |
| 4 | 12 | 13 | 12 | 1013 | 1013 < 1014 | low = 13 |
| 5 | 13 | 13 | 13 | 1014 | equal       | **FOUND at 13** |

Binary search: **5 comparisons**. Linear search would need **14**.
Same idea on 50,000 records: max 16 comparisons vs 50,000.

---

## Task 2 - Bubble sort (descending), first 3 passes
Input: first 10 amounts = `[1250, 2499, 320, 2499, 2499, 780, 5600, 150, 899, 899]`
(neighbours are swapped when the left one is smaller)

| | [0] | [1] | [2] | [3] | [4] | [5] | [6] | [7] | [8] | [9] |
|---|---|---|---|---|---|---|---|---|---|---|
| Start  | 1250 | 2499 | 320 | 2499 | 2499 | 780 | 5600 | 150 | 899 | 899 |
| Pass 1 | 2499 | 1250 | 2499 | 2499 | 780 | 5600 | 320 | 899 | 899 | **150** |
| Pass 2 | 2499 | 2499 | 2499 | 1250 | 5600 | 780 | 899 | 899 | **320** | 150 |
| Pass 3 | 2499 | 2499 | 2499 | 5600 | 1250 | 899 | 899 | **780** | 320 | 150 |

Each pass settles one more small value at the right end (150, then 320, then 780).
The large value 5600 moves only one place left per pass (position 6 -> 5 -> 4 -> 3),
which is why bubble sort needs so many passes. These rows match `outputs/example_task2_output.txt`.

### Merge sort dry run on `[1250, 2499, 320, 2499]` (descending)
```
Split:        [1250, 2499]        [320, 2499]
Split again:  [1250] [2499]       [320] [2499]
Merge pairs:  [2499, 1250]        [2499, 320]
Final merge:  compare 2499 vs 2499 (tie -> take LEFT, keeps order stable) -> 2499
              compare 1250 vs 2499 -> 2499
              compare 1250 vs 320  -> 1250
              leftover 320         -> 320
Result:       [2499, 2499, 1250, 320]
```

---

## Task 3 - Duplicate detection by sorting
Use 6 records. Key = (customerId, amount, minute).

| Order | Key |
|---|---|
| 1004 | (C104, 2499, 10:12) |
| 1014 | (C111, 1500, 12:05) |
| 1005 | (C104, 2499, 10:12) |
| 1015 | (C111, 1500, 12:06) |
| 1017 | (C113, 350, 13:10) |
| 1018 | (C114, 350, 13:10) |

**Step 1 - sort by key:** 1004, 1005, 1014, 1015, 1017, 1018 (equal keys are now neighbours)

**Step 2 - scan neighbours:**

| Compare | Same key? | current group | Action |
|---|---|---|---|
| 1005 vs 1004 | YES | [1004, 1005] | extend group |
| 1014 vs 1005 | no  | [1014] | previous group has 2 -> **SAVE [1004, 1005]** |
| 1015 vs 1014 | no (minute 12:05 vs 12:06) | [1015] | group of 1 -> discard |
| 1017 vs 1015 | no  | [1017] | discard |
| 1018 vs 1017 | no (different customer) | [1018] | discard |

**Result: one duplicate group -> orders 1004 and 1005.**
Notice 1014/1015 (minute boundary) and 1017/1018 (different customers) are correctly NOT flagged.

---

## Task 4 - Stack for undo (top of stack on the left)

| Action | Stack after | Book state |
|---|---|---|
| edit 1001 amount 1250 -> 1300 | [(1001, amount, 1250)] | 1001.amount = 1300 |
| edit 1002 customer C102 -> C999 | [(1002, customerId, C102), (1001, amount, 1250)] | 1002.customer = C999 |
| edit 1001 amount 1300 -> 1400 | [(1001, amount, 1300), (1002, ...), (1001, ...)] | 1001.amount = 1400 |
| UNDO -> pop (1001, amount, 1300) | [(1002, ...), (1001, ...)] | 1001.amount = **1300** |
| UNDO -> pop (1002, customerId, C102) | [(1001, amount, 1250)] | 1002.customer = **C102** |

The LAST edit is undone first = Last In, First Out.

### Queue for dispatch (head -> tail)

| Action | Queue |
|---|---|
| enqueue 1001 | 1001 |
| enqueue 1002 | 1001, 1002 |
| enqueue 1003 | 1001, 1002, 1003 |
| dequeue -> 1001 dispatched | 1002, 1003 |
| dequeue -> 1002 dispatched | 1003 |

First order in is the first order out = First In, First Out.

---

## Task 5 - Refund Rs 6 with denominations [1, 3, 4]

**Greedy:** take 4 (amount left 2) -> take 1 (left 1) -> take 1 (left 0) = **3 coins** (4+1+1)

**DP table** (`best[x]` = fewest coins to make x)

| x | tries | best[x] | choice |
|---|---|---|---|
| 0 | - | 0 | - |
| 1 | best[0]+1 | 1 | 1 |
| 2 | best[1]+1 | 2 | 1 |
| 3 | best[2]+1=3, best[0]+1=1 | 1 | 3 |
| 4 | best[3]+1=2, best[1]+1=2, best[0]+1=1 | 1 | 4 |
| 5 | best[4]+1=2, best[2]+1=3, best[1]+1=2 | 2 | 1 |
| 6 | best[5]+1=3, best[3]+1=2, best[2]+1=3 | **2** | 3 |

Walk back: x=6 -> take 3 -> x=3 -> take 3 -> x=0. Answer: **3 + 3 = 2 coins**. DP beats greedy.

### Greedy on Rs 2499 (Indian notes)
2499 -> 1x2000 (499 left) -> 2x200 (99 left) -> 1x50 (49) -> 2x20 (9) -> 1x5 (4) -> 2x2 (0) = **9 pieces**
