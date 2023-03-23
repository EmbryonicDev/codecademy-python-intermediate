
# Checkpoint 2
from roster import student_roster
import itertools
# Import modules above this line


class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)
        self.current_index = 0

    # Checkpoint 3
    def __iter__(self):
        return self

    # Checkpoint 3
    def __next__(self):
        if self.current_index >= len(self.sorted_names):
            raise StopIteration
        else:
            current_name = self.sorted_names[self.current_index]
            self.current_index += 1
            return current_name

    # Checkpoint 4
    def get_student_seating(self):
        # Generate all possible combinations of 5 tuples with 2 items from the names list
        combos = list(itertools.combinations(self.sorted_names, 2))
        return combos

    # Checkpoint 5
    def get_math_and_science_students(self):
        math_students = self.get_students_with_subject('Math')
        science_students = self.get_students_with_subject('Science')
        smart_students = itertools.chain(math_students, science_students)
        student_seating = itertools.combinations(smart_students, 4)
        return student_seating

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students
