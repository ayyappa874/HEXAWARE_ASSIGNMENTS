from task4_window import best_window_sliding
hourly = [12,18,25,31,44,52,60,71,66,58,49,40,35,38,47,63,80,92,85,70,55,40,28,19]
s, a = best_window_sliding(hourly)
print(f"Best window: hours {s}-{s+3}, average {a:.2f}")
