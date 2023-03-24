def student_counter():
    for i in range(1, 5001):
        yield i


student_generator = student_counter()
for student_id in student_generator:
    # Write your code below:

    print(student_id)
