def best_window_sliding(counts, k=4):
    """Start index and average of the k-hour window with highest average. O(n)."""
    if len(counts) < k:
        return -1, 0.0
    total = sum(counts[:k]); best_sum, best_start = total, 0
    for i in range(k, len(counts)):
        total += counts[i] - counts[i - k]
        if total > best_sum:
            best_sum, best_start = total, i - k + 1
    return best_start, best_sum / k

def best_window_brute(counts, k=4):
    """Recompute each window from scratch. O(n*k). Used to cross-check."""
    best_sum, best_start = None, -1
    for i in range(len(counts) - k + 1):
        s = sum(counts[i:i + k])
        if best_sum is None or s > best_sum:
            best_sum, best_start = s, i
    return best_start, (best_sum / k if best_sum is not None else 0.0)
