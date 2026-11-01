import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from common import *
from task1_bst import build
from task2_hashing import HashMap, find_duplicates, find_duplicates_pairwise, normalise
from task3_stages import bfs_shortest_path, find_cycle
from task4_window import longest_run_above, longest_run_brute
from task5_merge import merge_sorted

class T1(unittest.TestCase):
    def test_traversals(self):
        t = build(["CL1050","CL1020","CL1080","CL1010","CL1030"])
        self.assertEqual(t.inorder(), ["CL1010","CL1020","CL1030","CL1050","CL1080"])
        self.assertEqual(t.preorder(), ["CL1050","CL1020","CL1010","CL1030","CL1080"])
        self.assertEqual(t.postorder(), ["CL1010","CL1030","CL1020","CL1080","CL1050"])
    def test_empty(self):
        t = build([])
        self.assertEqual((t.inorder(), t.preorder(), t.postorder()), ([], [], []))
        self.assertEqual(t.search("X"), (False, 0))
    def test_duplicate_ignored(self):
        t = build(["B", "A", "B"]); self.assertEqual(t.size, 2)
        self.assertFalse(t.insert("A"))

class T2(unittest.TestCase):
    def test_groups(self):
        r = find_duplicates(load_claims())
        self.assertEqual([g for _, g in r], [["CL1010","CL1050","CL1100"], ["CL1030","CL1060"]])
    def test_different_date_not_duplicate(self):
        self.assertNotIn("CL1070", sum([g for _, g in find_duplicates(load_claims())], []))
    def test_empty(self):
        self.assertEqual(find_duplicates([]), [])
    def test_normalise(self):
        self.assertEqual(normalise(" pol -1001", "2026-10-12"), ("POL-1001", "2026-10-12"))
    def test_collision_handled(self):
        class One(HashMap):
            def _index(self, key): return 0
        self.assertEqual(find_duplicates(load_claims(), One()), find_duplicates(load_claims()))
    def test_pairwise_agrees(self):
        self.assertEqual(find_duplicates(load_claims()), find_duplicates_pairwise(load_claims()))

class T3(unittest.TestCase):
    def test_path(self):
        g = load_stage_graph()
        self.assertEqual(bfs_shortest_path(g, "REGISTRATION", "SETTLEMENT"), (["REGISTRATION","ASSESSMENT","SETTLEMENT"], 2))
        self.assertEqual(bfs_shortest_path(g, "SETTLEMENT", "REGISTRATION"), (None, -1))
        self.assertEqual(bfs_shortest_path(g, "SURVEYOR", "SURVEYOR"), (["SURVEYOR"], 0))
    def test_cycle(self):
        self.assertEqual(find_cycle(load_stage_graph()), ["ASSESSMENT","SURVEYOR","ASSESSMENT"])
    def test_no_cycle_and_empty(self):
        self.assertIsNone(find_cycle({"A": ["B"], "B": []}))
        self.assertIsNone(find_cycle({}))
    def test_self_loop(self):
        self.assertEqual(find_cycle({"A": ["A"]}), ["A", "A"])

class T4(unittest.TestCase):
    def test_run(self):
        d = load_daily_counts()
        self.assertEqual(longest_run_above(d), (6, 4))
        self.assertEqual(longest_run_above(d), longest_run_brute(d))
    def test_edges(self):
        self.assertEqual(longest_run_above([]), (-1, 0))
        self.assertEqual(longest_run_above([100, 50]), (-1, 0))      # 100 is not > 100
        self.assertEqual(longest_run_above([101, 101, 101]), (0, 3))
        self.assertEqual(longest_run_above([101, 5, 102, 103]), (2, 2))

class T5(unittest.TestCase):
    def test_merge(self):
        o = load_office_lists()
        self.assertEqual(merge_sorted(o["North"], o["South"]), sorted(o["North"] + o["South"]))
    def test_duplicates_kept_or_dropped(self):
        self.assertEqual(merge_sorted([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])
        self.assertEqual(merge_sorted([1, 2, 2], [2, 3], keep_duplicates=False), [1, 2, 3])
    def test_empty(self):
        self.assertEqual(merge_sorted([], []), [])
        self.assertEqual(merge_sorted([], [1, 2]), [1, 2])
        self.assertEqual(merge_sorted([1, 2], []), [1, 2])

if __name__ == "__main__":
    unittest.main()
