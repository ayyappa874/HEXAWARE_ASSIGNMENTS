# Example 5 - pairs that add up to a gift-card value
from task5_two_pointer import find_pairs

values = [100, 200, 300, 400, 500, 600, 700]      # must be sorted
print("Gift card 700:", find_pairs(values, 700))
print("Gift card 100:", find_pairs(values, 100))   # nothing adds up to 100
