dog_foods = {
    "Great Dane Foods": 4,
    "Min Pip Pup Foods": 10,
    "Pawsome Pup Foods": 8
}

# Write your code below:
dog_food_iterator = iter(dog_foods)
next_dog_food1 = next(dog_food_iterator)
next_dog_food2 = dog_food_iterator.__next__()
next_dog_food3 = dog_food_iterator.__next__()

for x in [next_dog_food1, next_dog_food2, next_dog_food3]:
    print(x)

# Will cause an error as there's nothing left to iterate
next(dog_food_iterator)
