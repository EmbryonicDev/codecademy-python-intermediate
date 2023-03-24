MAX_STUDENTS = 50


def get_student_ids():
    student_id = 1
    while student_id <= MAX_STUDENTS:
        # Write your code below
        yield student_id

        student_id += 1


student_id_generator = get_student_ids()
for i in student_id_generator:
    # Write your code below

    print(i)
