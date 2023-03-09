def print_animals(animal1, animal2, *args, animal4, **kwargs):
    print(animal1, animal2)
    print(args)
    print(animal4)
    print(kwargs)


print_animals('Snake', 'Fish', 'Guinea Pig',
              'Owl', animal4='Cat', animal5='Dog')


def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)


single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops',
                       sides='Mashed Potatoes', one='Vanilla', two="Cookies and Cream")
