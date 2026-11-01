# Example 4 - busiest 3 consecutive values in a short list
from task4_sliding_window import busiest_window

requests = [4, 7, 2, 9, 5, 8, 1, 6]
start, total = busiest_window(requests, 3)
print("Requests:", requests)
print(f"Busiest 3 in a row starts at position {start}: {requests[start:start + 3]} = {total}")
