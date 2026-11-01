"""Task 4 - Busiest continuous 3-hour window with a sliding window."""
import time
from common import load_traffic, minute_label


def busiest_window(counts, k):
    """Return (start_index, total) of the k consecutive values with the biggest sum.
    Add the value that enters the window, subtract the one that leaves. Ties -> earliest."""
    if k <= 0 or k > len(counts):
        raise ValueError("window size must be between 1 and the number of values")
    window = sum(counts[:k])
    best_total, best_start = window, 0
    for i in range(k, len(counts)):
        window += counts[i] - counts[i - k]
        if window > best_total:
            best_total, best_start = window, i - k + 1
    return best_start, best_total


def busiest_window_brute(counts, k):
    """Slow check: add up every window from scratch."""
    best_total, best_start = -1, 0
    for start in range(len(counts) - k + 1):
        total = sum(counts[start:start + k])
        if total > best_total:
            best_total, best_start = total, start
    return best_start, best_total


def main():
    per_minute = load_traffic()
    k = 3 * 60
    print(f"Loaded {len(per_minute)} per-minute values (24 hours). Window = {k} minutes (3 hours).")

    start, total = busiest_window(per_minute, k)
    end = start + k
    print("\nA) Per-minute data, sliding window")
    print(f"  Busiest 3 hours: {minute_label(start)} to {minute_label(end) if end < 1440 else '24:00'}")
    print(f"  Requests in the window: {total:,}  (average {total / k:,.0f} per minute)")
    print(f"  Whole day: {sum(per_minute):,} requests; the window holds {total / sum(per_minute) * 100:.1f}% of them")

    b_start, b_total = busiest_window_brute(per_minute, k)
    print(f"  Brute-force check gives the same answer: {(b_start, b_total) == (start, total)}")

    t0 = time.perf_counter()
    for _ in range(200):
        busiest_window(per_minute, k)
    t_slide = (time.perf_counter() - t0) / 200
    t0 = time.perf_counter()
    for _ in range(20):
        busiest_window_brute(per_minute, k)
    t_brute = (time.perf_counter() - t0) / 20
    print(f"  Time: sliding window {t_slide * 1e6:,.0f} us, brute force {t_brute * 1e6:,.0f} us "
          f"(about {t_brute / t_slide:.0f}x slower)")

    hourly = [sum(per_minute[h * 60:(h + 1) * 60]) for h in range(24)]
    h_start, h_total = busiest_window(hourly, 3)
    print("\nB) If only hourly totals were given (24 values, window of 3 hours)")
    print(f"  Busiest 3 hours: {h_start:02d}:00 to {h_start + 3:02d}:00, {h_total:,} requests")
    print("  (hourly data can only start on the hour, so its best window can only be equal or lower)")
    return {"start": minute_label(start), "end": minute_label(end), "total": total, "avg": total / k,
            "day_total": sum(per_minute), "share": total / sum(per_minute) * 100,
            "slide_us": t_slide * 1e6, "brute_us": t_brute * 1e6, "ratio": t_brute / t_slide,
            "hour_start": h_start, "hour_total": h_total}


if __name__ == "__main__":
    main()
