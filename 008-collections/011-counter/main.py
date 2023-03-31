from collections import Counter
from print_checkpoint import *

opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt',
                     'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress',
                     'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
# Checkpoint 1


def find_amount_sold(opening, closing, item):
    # Checkpoint 2
    opening_count = Counter(opening)
    closing_count = Counter(closing)
    # Checkpoint 3
    opening_count.subtract(closing_count)
    # Checkpoint 4
    return opening_count[item]


# Checkpoint 5
print_checkpoint(5)
tshirts_sold = find_amount_sold(
    opening_inventory, closing_inventory, 't-shirt')
print('tshirts_sold output:\n', tshirts_sold)
