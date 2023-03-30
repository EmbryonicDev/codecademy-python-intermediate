from print_checkpoint import *
from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Write your code below!
# Checkpoint 1
supplies_deque = deque()

print_checkpoint(2)
for x in csv_data:
    if x[2] == 'important':
        supplies_deque.appendleft(x)
    else:
        supplies_deque.append(x)
print('supplies_deque printed:\n', supplies_deque)

print_checkpoint(3)
ordered_important_supplies = deque()
for i in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())
print('ordered_important_supplies printed:\n', ordered_important_supplies)

print_checkpoint(4)
ordered_unimportant_supplies = deque()
for i in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())
print('ordered_unimportant_supplies printed:\n', ordered_unimportant_supplies)
