from print_checkpoint import *
from collections import *

overstock_items = [['shirt_103985', 15.99],
                   ['pants_906841', 19.99],
                   ['pants_765321', 15.99],
                   ['shoes_948059', 29.99],
                   ['shoes_356864', 9.99],
                   ['shirt_865327', 10.99],
                   ['shorts_086853', 9.99],
                   ['pants_267953', 21.99],
                   ['dress_976264', 32.99],
                   ['shoes_135786', 17.99],
                   ['skirt_196543', 12.99],
                   ['jacket_976535', 26.99],
                   ['pants_086367', 30.99],
                   ['dress_357896', 29.99],
                   ['shoes_157895', 14.99]]

# Write your code below!
# Checkpoints 1
split_prices = deque()

# Checkpoints 2
print_checkpoint(2)
for item in overstock_items:
    if item[1] > 20:
        split_prices.appendleft(item)
    else:
        split_prices.append(item)

print('split_prices printed:\n', split_prices)

# Checkpoints 3
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# Checkpoints 4
print_checkpoint(4)
bundles = []
while len(split_prices) >= 5:
    three_cheap_items = []
    two_expensive_items = []

    # Helper function
    def get_item(set_range, item_list, function):
        for x in range(set_range):
            item_list.append(function())

    # get cheap & expensive items
    get_item(3, three_cheap_items, split_prices.pop)
    get_item(2, two_expensive_items, split_prices.popleft)

    bundle_items = three_cheap_items+two_expensive_items
    bundle_price = sum(x[1] for x in bundle_items)

    bundles.append(ClothesBundle(bundle_items, bundle_price))

print('bundles printed:\n', bundles)


# Checkpoints 5
print_checkpoint(5)
promoted_bundles = [b for b in bundles if b.bundle_price > 100]

print('promoted_bundles printed:\n', promoted_bundles)
