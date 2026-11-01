import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from common import load_graph, load_scans
from task1_bst import build, height_experiment
from task2_hashmap import HashMap, build_lookup, find_double_scans
from task3_graph import bfs_shortest_path, dfs_reachable
from task4_window import best_window_sliding, best_window_brute
from task5_palindrome import is_palindrome_route

class T1(unittest.TestCase):
    def test_bst(self):
        t = build(["NAG","DEL","BOM","PNQ","HYD","BLR","MAA","CCU","AMD","JAI"])
        self.assertEqual(t.height(), 5)
        self.assertEqual(t.inorder(), sorted(t.inorder()))
        self.assertEqual(t.search("MAA"), (True, 4))
        self.assertFalse(t.search("XYZ")[0])
        self.assertFalse(t.insert("NAG"))
    def test_sorted_input_is_chain(self):
        s, r = height_experiment(200)
        self.assertEqual(s, 200); self.assertLess(r, 40)

class T2(unittest.TestCase):
    def test_hashmap_resize(self):
        m = HashMap()
        for i in range(500): m.put(f"k{i}", i)
        self.assertTrue(all(m.get(f"k{i}") == i for i in range(500)))
        self.assertIsNone(m.get("zzz"))
    def test_double_scans(self):
        r = find_double_scans(load_scans())
        self.assertEqual([x[0] for x in r], ["TRK1004", "TRK1006"])
    def test_same_parcel_different_time_not_double(self):
        r = find_double_scans(load_scans())
        self.assertNotIn("TRK1002", [x[0] for x in r])

class T3(unittest.TestCase):
    def test_bfs(self):
        g = load_graph()
        self.assertEqual(bfs_shortest_path(g, "PNQ", "CCU")[1], 3)
        self.assertEqual(bfs_shortest_path(g, "NAG", "JAI"), (None, -1))
        self.assertEqual(bfs_shortest_path(g, "NAG", "NAG"), (["NAG"], 0))
    def test_dfs(self):
        r = dfs_reachable(load_graph(), "NAG")
        self.assertEqual(len(r), 8); self.assertNotIn("AMD", r)

class T4(unittest.TestCase):
    def test_window(self):
        h = [12,18,25,31,44,52,60,71,66,58,49,40,35,38,47,63,80,92,85,70,55,40,28,19]
        self.assertEqual(best_window_sliding(h), (16, 81.75))
        self.assertEqual(best_window_sliding(h), best_window_brute(h))
    def test_short_input(self):
        self.assertEqual(best_window_sliding([1, 2, 3]), (-1, 0.0))

class T5(unittest.TestCase):
    def test_pal(self):
        self.assertTrue(is_palindrome_route("DEL-LED"))
        self.assertTrue(is_palindrome_route("Ab-C, c-BA"))
        self.assertFalse(is_palindrome_route("NAG-DEL-BOM"))
        self.assertTrue(is_palindrome_route(""))

if __name__ == "__main__":
    unittest.main()
