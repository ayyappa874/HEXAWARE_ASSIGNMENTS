import os, sys, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from task1_bst import *
from task2_hashmap import *
from task3_graph import *
from task4_window import *
from task5_palindrome import *

def main():
    hubs = load_hubs(); graph = load_graph(); scans = load_scans()
    print("=== TASK 1: BST OF HUB CODES ===")
    order = ["NAG","DEL","BOM","PNQ","HYD","BLR","MAA","CCU","AMD","JAI"]
    t = build(order)
    print("Insert order   :", order)
    print("In-order       :", t.inorder())
    print("Height (nodes) :", t.height())
    for c in ["MAA", "XYZ"]:
        print(f"Search {c}     :", t.search(c))
    print("Same codes, sorted input -> height:", build(sorted(order)).height())
    hs, hr = height_experiment(1000)
    print(f"1,000 codes: sorted input height {hs}, shuffled input height {hr}")
    codes = make_codes(1000)
    print("Search last code, sorted-input tree:", build(codes).search(codes[-1])[1], "comparisons")

    print("\n=== TASK 2: HASH MAP LOOKUP + DOUBLE SCANS ===")
    m = build_lookup(scans)
    print("Lookup TRK1003 :", m.get("TRK1003"))
    print("Lookup TRK9999 :", m.get("TRK9999"))
    print("Double scans   :", find_double_scans(scans))
    big = [{"trackingNo": f"TRK{i:06d}", "hubCode": "NAG", "scannedAt": "x"} for i in range(50000)]
    bm = build_lookup(big); ids = random.Random(1).sample(range(50000), 1000)
    t0 = time.perf_counter()
    for i in ids: bm.get(f"TRK{i:06d}")
    th = time.perf_counter() - t0
    t0 = time.perf_counter()
    for i in ids[:100]: linear_lookup(big, f"TRK{i:06d}")
    tl = (time.perf_counter() - t0) * 10
    print(f"50,000 parcels, 1,000 lookups: hash map {th*1000:.2f} ms, linear scan (est. from 100) {tl*1000:.1f} ms")

    print("\n=== TASK 3: GRAPH, BFS AND DFS ===")
    for h in hubs: print(f"{h['hubCode']} -> {graph[h['hubCode']]}")
    for a, b in [("MAA","DEL"), ("PNQ","CCU"), ("NAG","JAI")]:
        p, n = bfs_shortest_path(graph, a, b)
        print(f"BFS {a} to {b}: path={p} hops={n}")
    r = dfs_reachable(graph, "NAG")
    print("DFS from NAG   :", r, "count =", len(r))
    print("Not reachable  :", sorted(set(graph) - set(r)))

    print("\n=== TASK 4: SLIDING WINDOW ===")
    hourly = [12,18,25,31,44,52,60,71,66,58,49,40,35,38,47,63,80,92,85,70,55,40,28,19]
    s, a = best_window_sliding(hourly)
    print("Hourly counts  :", hourly)
    print(f"Best 4-hour window: hours {s} to {s+3}, counts {hourly[s:s+4]}, average {a:.2f}")
    print("Brute force agrees:", best_window_brute(hourly) == (s, a))
    rng = random.Random(3); big = [rng.randint(0, 500) for _ in range(200000)]
    t0 = time.perf_counter(); best_window_sliding(big); t1 = time.perf_counter() - t0
    t0 = time.perf_counter(); best_window_brute(big); t2 = time.perf_counter() - t0
    print(f"200,000 hours, k=4: sliding {t1*1000:.1f} ms, brute force {t2*1000:.1f} ms")
    t0 = time.perf_counter(); best_window_sliding(big[:50000], 1000); t1 = time.perf_counter() - t0
    t0 = time.perf_counter(); best_window_brute(big[:50000], 1000); t2 = time.perf_counter() - t0
    print(f"50,000 hours, k=1000: sliding {t1*1000:.1f} ms, brute force {t2*1000:.1f} ms")

    print("\n=== TASK 5: PALINDROME ROUTE CODES ===")
    for s in ["DEL-LED", "Ab-C, c-BA", "NAG-DEL-BOM", "MAA / aam", "", "-,-"]:
        print(f"{s!r:16} -> {is_palindrome_route(s)}")

if __name__ == "__main__":
    main()
