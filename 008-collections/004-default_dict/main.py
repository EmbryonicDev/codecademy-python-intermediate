from print_checkpoint import *
from collections import defaultdict

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress',
                    'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
# Checkpoint 1
validated_locations = defaultdict(lambda: 'TODO: Add to website')

# Checkpoint 2
validated_locations.update(site_locations)

print_checkpoint(3)
for product in updated_products:
    if product not in validated_locations:
        site_locations[product] = validated_locations[product]
print(site_locations)
