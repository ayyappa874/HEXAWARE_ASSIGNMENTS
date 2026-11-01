"""Run from the project root:  python -m unittest discover -s tests -v"""
import os, random, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
from common import load_categories, load_dependencies, load_traffic, load_order_values, generate_skus
from task1_bst import BST, build
from task2_hashing import ChainedHashTable
from task3_graph import deploy_order_dfs, deploy_order_bfs, is_valid_order
from task4_sliding_window import busiest_window, busiest_window_brute
from task5_two_pointer import find_pairs, find_pairs_brute


class T1(unittest.TestCase):
    def test_traversals(self):
        t = build(load_categories())
        self.assertEqual(t.inorder(), sorted(load_categories()))
        self.assertEqual(t.preorder()[0], "Grocery")
        self.assertEqual(t.postorder()[-1], "Grocery")
        self.assertEqual(t.size, 15)
        self.assertEqual(t.height(), 4)

    def test_search_and_duplicates(self):
        t = build(load_categories())
        self.assertEqual(t.search("Garden"), (True, 4))
        self.assertFalse(t.search("Laptops")[0])
        self.assertFalse(t.insert("Garden"))          # duplicate ignored
        self.assertEqual(t.size, 15)


class T2(unittest.TestCase):
    def test_collision_and_operations(self):
        t = ChainedHashTable(capacity=3, auto_resize=False)
        for i in range(6):
            t.put(f"K{i}", i)
        self.assertTrue(any(len(c) > 1 for c in t.buckets))
        self.assertEqual(t.get("K4"), 4)
        t.put("K4", 40)
        self.assertEqual(t.get("K4"), 40)
        self.assertTrue(t.remove("K4"))
        self.assertIsNone(t.get("K4"))
        self.assertEqual(t.size, 5)

    def test_matches_dict(self):
        data = generate_skus(3000)
        t, d = ChainedHashTable(), {}
        for sku, name, price in data:
            t.put(sku, name); d[sku] = name
        self.assertTrue(all(t.get(k) == v for k, v in d.items()))
        self.assertEqual(t.size, len(d))


class T3(unittest.TestCase):
    def test_valid_orders(self):
        deps = load_dependencies()
        for fn in (deploy_order_dfs, deploy_order_bfs):
            order, problem = fn(deps)
            self.assertIsNone(problem)
            self.assertTrue(is_valid_order(order, deps))
            self.assertEqual(len(order), 9)

    def test_cycle(self):
        deps = load_dependencies()
        deps["inventory"].append("cart")
        order, cycle = deploy_order_dfs(deps)
        self.assertIsNone(order)
        self.assertEqual(cycle[0], cycle[-1])
        self.assertEqual(set(cycle), {"cart", "pricing", "inventory"})
        order, stuck = deploy_order_bfs(deps)
        self.assertIsNone(order)
        self.assertTrue({"cart", "pricing", "inventory"} <= set(stuck))


class T4(unittest.TestCase):
    def test_matches_brute_force(self):
        rng = random.Random(1)
        for _ in range(200):
            data = [rng.randint(0, 50) for _ in range(rng.randint(3, 40))]
            k = rng.randint(1, len(data))
            self.assertEqual(busiest_window(data, k), busiest_window_brute(data, k))

    def test_real_data_and_errors(self):
        data = load_traffic()
        self.assertEqual(len(data), 1440)
        self.assertEqual(busiest_window(data, 180), busiest_window_brute(data, 180))
        self.assertEqual(busiest_window([4, 7, 2, 9, 5, 8, 1, 6], 3), (3, 22))
        with self.assertRaises(ValueError):
            busiest_window([1, 2], 3)


class T5(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(find_pairs(load_order_values(), 1000), [(150, 850), (250, 750), (400, 600), (500, 500)])
        self.assertEqual(find_pairs([100, 200, 300], 50), [])

    def test_matches_brute_force(self):
        rng = random.Random(2)
        for _ in range(300):
            data = sorted(rng.randint(1, 30) for _ in range(rng.randint(2, 25)))
            target = rng.randint(2, 60)
            self.assertEqual(find_pairs(data, target), find_pairs_brute(data, target))


if __name__ == "__main__":
    unittest.main()
