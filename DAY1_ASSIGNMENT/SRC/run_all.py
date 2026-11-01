"""Run all 5 tasks and save the console output into /outputs (deliverable)."""
import io
import os
from contextlib import redirect_stdout
import task1_search, task2_sorting, task3_duplicates, task4_stack_queue, task5_refund

TASKS = [("task1_output.txt", task1_search), ("task2_output.txt", task2_sorting),
         ("task3_output.txt", task3_duplicates), ("task4_output.txt", task4_stack_queue),
         ("task5_output.txt", task5_refund)]
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for fname, mod in TASKS:
        buf = io.StringIO()
        with redirect_stdout(buf):
            mod.main()
        text = buf.getvalue()
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"===== {mod.__name__} =====\n{text}")
