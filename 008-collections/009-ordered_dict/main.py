from print_checkpoint import *
from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!
# Checkpoint 1
orders = OrderedDict(order_data)

# Checkpoint 2
print_checkpoint(2)
to_move = []
to_remove = []
for order, status in orders.items():
    if status == 'returned':
        to_move.append(order)
    elif status == 'canceled':
        to_remove.append(order)
print('to_move printed:\n', to_move)
print('\nto_remove printed:\n', to_remove)

# Checkpoint 3
print_checkpoint(3)
for order in to_remove:
    orders.pop(order)
print('orders printed after removing cancelled items:\n', orders)

# Checkpoint 4
print_checkpoint(4)
for order in to_move:
    orders.move_to_end(order)
print('orders printed after moving returned items to end:\n', orders)
