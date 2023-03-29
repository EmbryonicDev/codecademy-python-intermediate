import random

guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        yield name


print(f"\nCheckpoint 1")
guest_list_generator = read_guestlist('guest_list.txt')
for i in range(10):
    print(f"{i+1}: {next(guest_list_generator)}")

# Checkpoint 2
guest_list_generator.send('Jane,35')

print(f"\nCheckpoint 3")
for i in guest_list_generator:
    print(i)

print(f"\nCheckpoint 4")
over_21 = (name for name, age in guests.items() if age >= 21)
for name in over_21:
    print(name, "is 21 or older")


print(f"\nCheckpoint 5")


def table_generator(table_num):
    foods = ['Chicken', 'Beef', 'Fish']
    for i in range(1, 6):
        yield (random.choice(foods), f'Table {table_num}', f'Seat {i}')


table_1 = table_generator(1)
table_2 = table_generator(2)
table_3 = table_generator(3)

for i in range(5):
    print(next(table_1))
for i in range(5):
    print(next(table_2))
for i in range(5):
    print(next(table_3))
