def merge_sorted(a, b, keep_duplicates=True):
    """Two pointers over two already sorted lists. No sort() call."""
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            nxt = a[i]; i += 1
        else:
            nxt = b[j]; j += 1
        if keep_duplicates or not out or out[-1] != nxt:
            out.append(nxt)
    for x in a[i:] + b[j:]:           # one list is empty; copy the other
        if keep_duplicates or not out or out[-1] != x:
            out.append(x)
    return out
