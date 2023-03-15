class School:
    def __init__(self, name: str, numberOfStudents: int, level: str):
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


class Primary(School):
    def __init__(self, name, numberOfStudents, level='primary'):
        School.__init__(self, name, numberOfStudents, level)
        self._pickupPolicy = "Pick up at 3pm"

    @property
    def pickupPolicy(self):
        return self._pickupPolicy


if __name__ == "__main__":
    print(f"\nTesting class School\n")
    s1 = School('White Horse', 96, 'primary')
    print(s1)
    s1.numberOfStudents = 13

    print(f"\nTesting class Primary\n")
    p1 = Primary('Primary 1', 64, 'primary')
    print(p1)
    p1.numberOfStudents = 69
    print(p1.pickupPolicy)
