"""Run:  python -m unittest discover -s tests -v   (from the project root)"""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
from common import load_orders, generate_orders, DATA_DIR
from task1_search import linear_search, binary_search
from task2_sorting import bubble_sort_desc, merge_sort_desc
from task3_duplicates import find_duplicates, minute_of
from task4_stack_queue import Stack, Queue
from task5_refund import greedy_change, dp_change, count, INR

SAMPLE = load_orders(os.path.join(DATA_DIR, "orders_20.csv"))


class T1(unittest.TestCase):
    def test_search_agree(self):
        for o in SAMPLE:
            self.assertEqual(linear_search(SAMPLE, o["orderId"])[0], binary_search(SAMPLE, o["orderId"])[0])
        self.assertEqual(binary_search(SAMPLE, 9999)[0], -1)


class T2(unittest.TestCase):
    def test_sorts(self):
        expect = sorted([o["amount"] for o in SAMPLE], reverse=True)
        self.assertEqual([o["amount"] for o in bubble_sort_desc(SAMPLE)], expect)
        self.assertEqual([o["amount"] for o in merge_sort_desc(SAMPLE)], expect)


class T3(unittest.TestCase):
    def test_sample_groups(self):
        groups = sorted(sorted(o["orderId"] for o in g) for g in find_duplicates(SAMPLE))
        self.assertEqual(groups, [[1004, 1005], [1009, 1010, 1011]])

    def test_against_brute_force(self):
        rows = generate_orders(400, seed=3)
        for i in range(0, 400, 7):                       # plant extra duplicates
            rows[i]["customerId"], rows[i]["amount"] = "CX", 123
        k = lambda o: (o["customerId"], o["amount"], minute_of(o["createdAt"]))
        brute = {a["orderId"] for a in rows for b in rows if a is not b and k(a) == k(b)}
        fast = {o["orderId"] for g in find_duplicates(rows) for o in g}
        self.assertEqual(fast, brute)


class T4(unittest.TestCase):
    def test_stack_lifo_queue_fifo(self):
        s, q = Stack(), Queue()
        for i in range(5): s.push(i); q.enqueue(i)
        self.assertEqual([s.pop() for _ in range(5)], [4, 3, 2, 1, 0])
        self.assertEqual([q.dequeue() for _ in range(5)], [0, 1, 2, 3, 4])
        with self.assertRaises(IndexError): s.pop()
        with self.assertRaises(IndexError): q.dequeue()


class T5(unittest.TestCase):
    def test_greedy_fails_dp_wins(self):
        self.assertEqual(count(greedy_change(6, [1, 3, 4])), 3)
        self.assertEqual(count(dp_change(6, [1, 3, 4])), 2)

    def test_inr_greedy_optimal(self):
        for a in range(1, 2000):
            self.assertEqual(count(greedy_change(a, INR)), count(dp_change(a, INR)))


if __name__ == "__main__":
    unittest.main()
