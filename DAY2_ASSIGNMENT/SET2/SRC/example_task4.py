from common import load_daily_counts
from task4_window import longest_run_above
s, n = longest_run_above(load_daily_counts())
print(f"Longest run: start day {s}, {n} days")
