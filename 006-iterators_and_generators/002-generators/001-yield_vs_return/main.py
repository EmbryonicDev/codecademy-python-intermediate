def class_standing_generator():
    yield 'Freshman'
    yield 'Sophomore'
    yield 'Junior'
    yield 'Senior'


class_standings = class_standing_generator()

for x in class_standings:
    print(x)
