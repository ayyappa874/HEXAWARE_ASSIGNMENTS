# Day 1 - Set 2: Insurance Claims Processing

Segue 2027 - Python Foundation. Problem Solving Techniques and Data Structures - II.

| Task | File | Technique |
|------|------|-----------|
| 1 | `src/task1_bst.py` | BST of claim IDs, inorder / preorder / postorder |
| 2 | `src/task2_hashing.py` | Normalised key + hash map (chaining) for duplicate claims |
| 3 | `src/task3_stages.py` | Directed graph of approval stages, BFS shortest path, DFS loop detection |
| 4 | `src/task4_window.py` | Sliding window, longest run of days above 100 claims |
| 5 | `src/task5_merge.py` | Two-pointer merge of two sorted lists |

## Run
```
cd src
python run_all.py            # all five tasks, prints output
python example_task1.py      # small example per task (1 to 5)
cd ..
python -m unittest discover -s tests -v
```
Python 3.8+, no extra packages. 18 tests (empty input and duplicates covered).

## Folders
- `data/` claims_12.csv, stages.csv, daily_claims_14.csv, office_lists.csv
- `outputs/` saved real console output
- `docs/pseudocode.md` pseudocode for all tasks
- `Insurance_Claims_Practical_Record.docx` full practical record
