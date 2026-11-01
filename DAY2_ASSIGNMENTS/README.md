# E-Commerce Catalogue and Traffic Analysis - Problem Solving Techniques & Data Structures II

Hexaware training | Day 2 | Python 3.9+ (standard library only)

An e-commerce platform wants faster category browsing, instant SKU look-ups and a way to size its infrastructure for peak traffic. This project solves five problems with the right data structure or pattern, then tests and measures each one.

The full written record is in **[docs/Ecommerce_Catalogue_Day2_Practical_Record.docx](docs/Ecommerce_Catalogue_Day2_Practical_Record.docx)**: for each task it has the pseudocode, Python code, an example with real output, the execution output, a dry run, complexity and key takeaways. The decision table is in [docs/decision_table.md](docs/decision_table.md).

## Project structure
```
day2-ecommerce-catalogue/
├── README.md
├── data/
│   ├── categories_15.csv        # Task 1 - 15 product categories (in insert order)
│   ├── skus_20.csv              # Task 2 - 20 sample SKUs (100,000 more are generated at run time)
│   ├── dependencies.csv         # Task 3 - 9 microservices and what each depends on
│   ├── traffic_24h.csv          # Task 4 - requests per minute for 24 hours (1,440 rows)
│   └── order_values_20.csv      # Task 5 - 20 sorted order values
├── src/
│   ├── common.py                # file loaders and the 100,000-SKU generator
│   ├── make_data.py             # re-creates the small data files
│   ├── task1_bst.py             # Binary Search Tree + 3 traversals
│   ├── task2_hashing.py         # chained hash table vs dict
│   ├── task3_graph.py           # deployment order with DFS / BFS + cycle detection
│   ├── task4_sliding_window.py  # busiest 3-hour window
│   ├── task5_two_pointer.py     # gift-card pairs
│   ├── example_task1..5.py      # short examples, one per task
│   └── run_all.py               # runs all tasks, saves output and metrics.json
├── tests/test_all.py            # 10 unit tests
├── outputs/                     # saved console output (tasks and examples)
└── docs/
    ├── Ecommerce_Catalogue_Day2_Practical_Record.docx
    ├── pseudocode.md            # FUNCTION ... END FUNCTION style
    └── decision_table.md
```

## How to run
```bash
cd src
python run_all.py                 # runs all 5 tasks, writes ../outputs/*.txt
python example_task1.py           # a small example per task (1 to 5)

cd ..
python -m unittest discover -s tests -v
```

## Assumptions
- **Task 3:** an arrow such as `cart -> pricing` means "cart depends on pricing", so pricing is deployed first.
- **Task 4:** "requests-per-minute for 24 hours" is 1,440 values, so a 3-hour window is 180 minutes. The hourly version (24 values, window of 3) is shown too.
- **Task 5:** each different pair of values is listed once; the input list must be sorted.

## Results from one run
Timings depend on the computer; the comparisons between methods do not.

| Task | What was built | Result |
|---|---|---|
| 1 | Binary Search Tree, 3 traversals | Inorder is alphabetical; search needs 4 comparisons in the balanced tree but 15 when categories are inserted A to Z (height 15) |
| 2 | Hash table with chaining vs dict | 100,000 look-ups: own table 2.05 us each, dict 0.33 us (6.3x faster), list scan 1,321 us |
| 3 | Graph, DFS and BFS | Both give valid orders; DFS names the loop `cart -> pricing -> inventory -> cart`, BFS lists 6 blocked services |
| 4 | Sliding window | Busiest 3 hours 18:33 to 21:33: 242,229 requests (41.2% of the day); about 10x faster than brute force |
| 5 | Two pointers | 4 pairs for a Rs 1,000 gift card; 5,000 values: 0.38 ms vs 647.8 ms brute force |

## Key takeaways
1. Pick the structure that matches the question: BST, hash table, graph, sliding window, two pointers.
2. Tree shape matters: 4 comparisons when balanced, 15 when inserted in sorted order.
3. Hashing makes look-ups almost instant; the built-in dict beat our own table.
4. A graph gives an order and a loop check; DFS shows the exact loop, BFS only shows blocked services.
5. Do not repeat work: sliding window and two pointers beat brute force.
6. Check each method's condition: good insert order, sorted data, fine-grained data.
7. Benchmark honestly: one run on one machine.

## Limits
Traffic data and the 100,000 SKUs are generated, not real. Each timing is a single run (the list-scan used 200 look-ups only). The BST does not balance itself. Task 5 counts different value pairs once.
