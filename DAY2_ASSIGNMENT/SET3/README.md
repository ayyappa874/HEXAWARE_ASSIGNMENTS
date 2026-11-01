# Day 1 - Set 3: Logistics Network and Delivery Windows

Segue 2027 - Python Foundation. Problem Solving Techniques and Data Structures - II.

| Task | File | Technique |
|------|------|-----------|
| 1 | `src/task1_bst.py` | BST of hub codes: insert, search, height, effect of sorted input |
| 2 | `src/task2_hashmap.py` | Hash map for tracking numbers, double-scan check |
| 3 | `src/task3_graph.py` | Adjacency list, BFS fewest hops, DFS reachability |
| 4 | `src/task4_window.py` | Sliding window, best 4-hour average |
| 5 | `src/task5_palindrome.py` | Two-pointer palindrome of route codes |

## Run
```
cd src
python run_all.py            # all five tasks, prints output
python example_task1.py      # small example per task (1 to 5)
cd ..
python -m unittest discover -s tests -v
```
Python 3.8+, no extra packages.

## Folders
- `data/` hubs_10.csv, scans_12.csv
- `outputs/` saved real console output
- `docs/pseudocode.md` pseudocode for all tasks
- `Logistics_Network_Practical_Record.docx` full practical record
