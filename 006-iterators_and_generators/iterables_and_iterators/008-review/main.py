# Write your code below:
# Checkpoint 4
import itertools


# Checkpoint 1
cat_toys = [('laser', 1.99), ('fountain', 5.99),
            ('scratcher', 10.99), ('catnip', 15.99)]

# Checkpoint 2
cat_toy_iterator = iter(cat_toys)

# Checkpoint 3
for i in range(len(cat_toys)):
    print(next(cat_toy_iterator))

max_money = 15
options = []

# Checkpoint 5
toy_combos = itertools.combinations(cat_toys, 2)

#    toy2 = combo[1]
#    cost_of_toy2 = toy2[1]
