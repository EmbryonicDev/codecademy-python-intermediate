# Write your code below:

import itertools

max_capacity = 1000
num_bags = 0

for x in itertools.count(start=13.5, step=13.5):
    if x >= max_capacity:
        break
    num_bags += 1
    print(f"Total bags: {num_bags} = {x}lbs\n")

print(num_bags)
