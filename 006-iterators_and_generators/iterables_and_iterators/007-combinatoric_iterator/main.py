import itertools

collars = ["Red-S", "Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# Write your code below:
# Unique combinations of 3 will be created, each in its own tuple
collar_combo_iterator = itertools.combinations(collars, 3)

# print all unique tuples
for combo in collar_combo_iterator:
    print(combo)
