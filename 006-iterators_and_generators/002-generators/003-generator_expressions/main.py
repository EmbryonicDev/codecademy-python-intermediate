def cs_generator():
    for i in range(1, 5):
        yield "Computer Science " + str(i)


# Write your code below:
cs_courses = cs_generator()
print('\nCheckpoint 1')
for x in cs_courses:
    print(x)

# Checkpoint 2
cs_generator_exp = ("Computer Science " + str(x) for x in range(1, 5))

print('\nCheckpoint 3')
for x in cs_generator_exp:
    print(x)
