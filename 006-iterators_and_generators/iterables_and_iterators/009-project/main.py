# Checkpoint 1
import random
from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools
from itertools import permutations

student_iterator = iter(student_roster)
for i in range(len(student_roster)):
    print(next(student_iterator))

# Checkpoint 3
print('\nCheckpoint 3\n')
organizer = ClassroomOrganizer()
for student_name in organizer:
    print(student_name)

# Checkpoint 4
student_seating = organizer.get_student_seating()

print()
print('\nCheckpoint 4\n')
# print each list item\
for combo in student_seating:
    print(combo)


# Checkpoint 5
print(f'\nCheckpoint 5\n')
for combo in organizer.get_math_and_science_students():
    print(combo)
