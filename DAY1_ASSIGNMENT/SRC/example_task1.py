# Example 1 - find order 1014 in the 20 sample records
from common import load_sample
from task1_search import linear_search, binary_search

orders = load_sample()

pos, steps = linear_search(orders, 1014)
print(f"Linear search : found at position {pos} after {steps} comparisons")

pos, steps = binary_search(orders, 1014)
print(f"Binary search : found at position {pos} after {steps} comparisons")
print("Order details :", orders[pos])

pos, steps = binary_search(orders, 9999)
print(f"Order 9999    : position {pos} (-1 means not found) after {steps} comparisons")
