"""Run all 5 tasks, save the console output in /outputs (and the numbers in metrics.json)."""
import io
import json
import os
from contextlib import redirect_stdout
import task1_bst, task2_hashing, task3_graph, task4_sliding_window, task5_two_pointer

TASKS = [(1, task1_bst), (2, task2_hashing), (3, task3_graph), (4, task4_sliding_window), (5, task5_two_pointer)]
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    metrics = {}
    for n, mod in TASKS:
        buf = io.StringIO()
        with redirect_stdout(buf):
            metrics[f"t{n}"] = mod.main()
        text = buf.getvalue()
        with open(os.path.join(OUT, f"task{n}_output.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"===== task {n}: {mod.__name__} =====\n{text}")
    with open(os.path.join(OUT, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=1)
