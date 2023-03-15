class School:
    def __init__(self, name: str, level: str, numberOfStudents: int):
        self._name = name
        self._level = level
        self._numberOfStudents = numberOfStudents

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def numberOfStudents(self):
        return self._numberOfStudents

    @numberOfStudents.setter
    def numberOfStudents(self, new_students_added: int):
        if isinstance(new_students_added, int):
            self._numberOfStudents = new_students_added
            print((
                f"{self.name} has {self.numberOfStudents} {'students' if new_students_added > 1 else 'student'}").title())
        else:
            print("Please enter a Valid Number")

    def __repr__(self):
        return (f"{self.level.title()} school: {self.name}, presently has {self.numberOfStudents} students").title()


if __name__ == "__main__":
    s1 = School('White Horse', 'primary', 96)
    print(s1)
    s1.numberOfStudents = 13
