import os, sys, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from task1_bst import *
from task2_hashing import *
from task3_stages import *
from task4_window import *
from task5_merge import *

def main():
    claims = load_claims(); graph = load_stage_graph()
    daily = load_daily_counts(); offices = load_office_lists()
    print("=== TASK 1: BST OF CLAIM IDS ===")
    ids = [c["claimId"] for c in claims]
    t = build(ids)
    print("Insert order :", ids)
    print("Inorder      :", t.inorder())
    print("Preorder     :", t.preorder())
    print("Postorder    :", t.postorder())
    print("Inorder sorted:", t.inorder() == sorted(ids))
    for k in ["CL1065", "CL9999"]:
        print(f"Search {k}  :", t.search(k))
    print("Insert CL1050 again ->", t.insert("CL1050"), "(False = duplicate ignored)")

    print("\n=== TASK 2: HASHING FOR DUPLICATE CLAIMS ===")
    for key, grp in find_duplicates(claims):
        print("Duplicate group", key, "->", grp)
    print("Pairwise check agrees:", find_duplicates(claims) == find_duplicates_pairwise(claims))
    tbl = HashMap(); find_duplicates(claims, tbl)
    print(f"Table after 12 claims: {tbl.size} keys, {len(tbl.buckets)} buckets, "
          f"{tbl.collisions()} collisions, longest chain {tbl.longest_chain()}")
    class OneBucket(HashMap):
        def _index(self, key): return 0
    forced = OneBucket(); r = find_duplicates(claims, forced)
    print(f"Forced collision (all keys in 1 bucket): chain {forced.longest_chain()}, same result: {r == find_duplicates(claims)}")
    rng = random.Random(5)
    big = [{"claimId": f"C{i}", "policyNo": f"POL-{rng.randint(1, 3000)}", "incidentDate": "2026-10-12"} for i in range(5000)]
    t0 = time.perf_counter(); h = find_duplicates(big); th = time.perf_counter() - t0
    t0 = time.perf_counter(); p = find_duplicates_pairwise(big); tp = time.perf_counter() - t0
    print(f"5,000 claims: hashing {th*1000:.1f} ms, pairwise {tp*1000:.0f} ms, same answer: {h == p}")

    print("\n=== TASK 3: APPROVAL STAGES AS DIRECTED GRAPH ===")
    for u, vs in graph.items(): print(f"{u} -> {vs}")
    for a, b in [("REGISTRATION", "SETTLEMENT"), ("SURVEYOR", "SETTLEMENT"), ("SETTLEMENT", "REGISTRATION")]:
        print(f"BFS {a} to {b}:", bfs_shortest_path(graph, a, b))
    print("Loop found   :", find_cycle(graph))
    nl = {"REGISTRATION": ["ASSESSMENT"], "ASSESSMENT": ["SURVEYOR"], "SURVEYOR": ["SETTLEMENT"], "SETTLEMENT": []}
    print("Loop found (no rework edge):", find_cycle(nl))

    print("\n=== TASK 4: LONGEST RUN ABOVE 100 CLAIMS ===")
    print("Daily claims :", daily)
    s, n = longest_run_above(daily)
    print(f"Longest run  : days {s} to {s+n-1} ({n} days), counts {daily[s:s+n]}")
    print("Brute force agrees:", longest_run_brute(daily) == (s, n))
    rng = random.Random(3); bigd = [rng.randint(0, 200) for _ in range(1000000)]
    t0 = time.perf_counter(); a = longest_run_above(bigd); t1 = time.perf_counter() - t0
    print(f"1,000,000 days: sliding window {t1*1000:.0f} ms, run length {a[1]}")
    allhigh = [150] * 3000
    t0 = time.perf_counter(); longest_run_above(allhigh); t1 = time.perf_counter() - t0
    t0 = time.perf_counter(); longest_run_brute(allhigh); t2 = time.perf_counter() - t0
    print(f"3,000 days all above 100 (worst case): sliding {t1*1000:.2f} ms, brute force {t2*1000:.0f} ms")

    print("\n=== TASK 5: MERGE TWO SORTED LISTS ===")
    a, b = offices["North"], offices["South"]
    print("North        :", a); print("South        :", b)
    print("Merged       :", merge_sorted(a, b))
    print("Merged unique:", merge_sorted(a, b, keep_duplicates=False))
    print("Empty + list :", merge_sorted([], b))
    print("Both empty   :", merge_sorted([], []))
    A = sorted(rng.sample(range(2000000), 200000)); B = sorted(rng.sample(range(2000000), 200000))
    t0 = time.perf_counter(); m = merge_sorted(A, B); t1 = time.perf_counter() - t0
    t0 = time.perf_counter(); m2 = sorted(A + B); t2 = time.perf_counter() - t0
    print(f"200,000 + 200,000 IDs: two-pointer merge {t1*1000:.0f} ms, concat + sorted() {t2*1000:.0f} ms, same result: {m == m2}")

if __name__ == "__main__":
    main()
