import itertools

great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]

# Write your code below:
all_skus_iterator = itertools.chain(
    great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for x in all_skus_iterator:
    print(x)
