def course_generator():
    yield ("Computer Science", 5)
    # Write your code below:
    yield ("Art", 10)
    yield ("Business", 15)


def add_five_students(courses):
    for course in courses:
        yield (course[0], course[1]+5)


increased_courses = add_five_students(course_generator())
for course in increased_courses:
    print(f"{course[0]} with {course[1]+5} students")
