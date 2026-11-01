# Example 4 - Stack for "undo last edit" and Queue for dispatch
from common import load_sample
from task4_stack_queue import Stack, Queue

orders = {o["orderId"]: o for o in load_sample()}

undo = Stack()
for new_amount in (1300, 1400):                    # two edits to order 1001
    undo.push((1001, orders[1001]["amount"]))      # remember the OLD amount
    orders[1001]["amount"] = new_amount
    print("Edited order 1001 amount to", new_amount)

order_id, old_amount = undo.pop()                  # undo the LAST edit only
orders[order_id]["amount"] = old_amount
print("Undo -> order 1001 amount is back to", orders[1001]["amount"])

line = Queue()
for order_id in (1001, 1002, 1003):
    line.enqueue(order_id)
print("Dispatch order:", [line.dequeue(), line.dequeue(), line.dequeue()])
