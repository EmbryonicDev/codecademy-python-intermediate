from print_checkpoint import *
from collections import namedtuple

clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
# Checkpoint 1
ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

# Checkpoint 2
new_coat = ClothingItem('coat', 'black', 'small', 14.99)

# Checkpoint 3
coat_cost = new_coat.price

print_checkpoint(4)
updated_clothes_data = []
for item in clothes:
    updated_clothes_data.append(ClothingItem(
        item[0], item[1], item[2], item[3]))
print('updated_clothes_data printed:\n', updated_clothes_data)
