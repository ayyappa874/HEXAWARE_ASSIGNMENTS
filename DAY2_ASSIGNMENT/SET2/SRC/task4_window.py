def longest_run_above(counts, limit=100):
    """Longest run of consecutive days with counts > limit.
    Variable-size sliding window: right edge moves every day, left edge
    jumps past any day that is not above the limit.
    Returns (start_day, length); (-1, 0) if no day exceeds the limit."""
    best_len, best_start, left = 0, -1, 0
    for right, c in enumerate(counts):
        if c <= limit:
            left = right + 1
        elif right - left + 1 > best_len:
            best_len, best_start = right - left + 1, left
    return best_start, best_len

def longest_run_brute(counts, limit=100):
    """Check every start day. O(n^2) worst case. Cross-check only."""
    best_len, best_start = 0, -1
    for i in range(len(counts)):
        j = i
        while j < len(counts) and counts[j] > limit:
            j += 1
        if j - i > best_len:
            best_len, best_start = j - i, i
    return best_start, best_len
