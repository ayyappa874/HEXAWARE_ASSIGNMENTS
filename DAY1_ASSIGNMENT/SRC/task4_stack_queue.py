"""Task 4 - Custom Stack (undo order edit) and Queue (dispatch line) vs built-ins."""
import os
import time
from collections import deque
from common import load_orders, DATA_DIR


class _Node:
    __slots__ = ("value", "next")
    def __init__(self, value, nxt=None):
        self.value, self.next = value, nxt


class Stack:
    """LIFO using a singly linked list. push/pop/peek are all O(1)."""
    def __init__(self):
        self._top, self._size = None, 0
    def push(self, v):
        self._top = _Node(v, self._top); self._size += 1
    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack")
        v = self._top.value; self._top = self._top.next; self._size -= 1
        return v
    def peek(self):
        if self._top is None:
            raise IndexError("peek from empty stack")
        return self._top.value
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return self._size


class Queue:
    """FIFO using a linked list with head AND tail pointers. enqueue/dequeue O(1)."""
    def __init__(self):
        self._head = self._tail = None
        self._size = 0
    def enqueue(self, v):
        node = _Node(v)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node; self._tail = node
        self._size += 1
    def dequeue(self):
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        v = self._head.value; self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return v
    def is_empty(self):
        return self._size == 0
    def __len__(self):
        return self._size


def demo_undo(orders):
    print("A) UNDO LAST ORDER EDIT (custom Stack)")
    book = {o["orderId"]: dict(o) for o in orders}
    history = Stack()

    def edit(oid, field, new):
        history.push((oid, field, book[oid][field]))      # remember OLD value
        book[oid][field] = new
        print(f"  edit  order {oid}: {field} -> {new}")

    def undo():
        oid, field, old = history.pop()
        book[oid][field] = old
        print(f"  undo  order {oid}: {field} restored to {old}")

    edit(1001, "amount", 1300)
    edit(1002, "customerId", "C999")
    edit(1001, "amount", 1400)
    undo(); undo()
    print(f"  order 1001 amount now {book[1001]['amount']} (expected 1300), "
          f"order 1002 customer {book[1002]['customerId']} (expected C102)")
    assert book[1001]["amount"] == 1300 and book[1002]["customerId"] == "C102"


def demo_dispatch(orders):
    print("\nB) DISPATCH LINE (custom Queue, first come first served)")
    q = Queue()
    for o in orders[:5]:
        q.enqueue(o["orderId"]); print(f"  enqueue order {o['orderId']}")
    while not q.is_empty():
        print(f"  dispatch order {q.dequeue()}  (remaining {len(q)})")


def bench(label, fn):
    t0 = time.perf_counter(); fn()
    dt = time.perf_counter() - t0
    print(f"  {label:<38}{dt:>8.4f} s")
    return dt


def main():
    orders = load_orders(os.path.join(DATA_DIR, "orders_20.csv"))
    demo_undo(orders)
    demo_dispatch(orders)

    N = 200_000
    print(f"\nC) COMPARISON: custom vs built-in ({N:,} operations each)")

    def custom_stack():
        s = Stack()
        for i in range(N): s.push(i)
        while not s.is_empty(): s.pop()

    def list_stack():
        s = []
        for i in range(N): s.append(i)
        while s: s.pop()

    def custom_queue():
        q = Queue()
        for i in range(N): q.enqueue(i)
        while not q.is_empty(): q.dequeue()

    def deque_queue():
        q = deque()
        for i in range(N): q.append(i)
        while q: q.popleft()

    def list_pop0_queue():
        q = list(range(50_000))              # smaller N: this one is O(n^2) overall
        while q: q.pop(0)

    bench("Custom Stack (linked list)", custom_stack)
    bench("Built-in list as stack", list_stack)
    bench("Custom Queue (linked list)", custom_queue)
    bench("Built-in collections.deque as queue", deque_queue)
    bench("list.pop(0) as queue (50,000 only)", list_pop0_queue)

    print("\nObservations:")
    print("  - Built-ins are faster (written in C); custom classes pay Python-call overhead.")
    print("  - All four are O(1) per operation; only list.pop(0) is O(n) per op (shifts all items).")
    print("  - Use list for stacks, deque for queues; never list.pop(0) for a real queue.")


if __name__ == "__main__":
    main()
