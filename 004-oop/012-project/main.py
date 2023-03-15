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
                f"{self.name} has {self.numberOfStudents} {'students' if self.numberOfStudents > 1 else 'student'}").title())
        else:
            print("Please enter a Valid Number")

    def __repr__(self):
        return (f"{self.level} school: {self.name}, presently has {self.numberOfStudents} {'students' if self.numberOfStudents > 1 else 'student'}").title()


class Primary(School):
    def __init__(self, name, level, numberOfStudents):
        super().__init__(name, level, numberOfStudents)
        self._pickupPolicy = "Pick up at 3pm"

    @property
    def pickupPolicy(self):
        return self._pickupPolicy

    def __repr__(self):
        return f"{super().__repr__()}\n{self.pickupPolicy}"


class Middle(School):
    def __init__(self, name, level, numberOfStudents):
        super().__init__(name, level, numberOfStudents)


class High(School):
    def __init__(self, name, level, numberOfStudents, *sportsTeams):
        super().__init__(name, level, numberOfStudents)
        self._sportsTeams = list(sportsTeams)[0]

    @property
    def sportsTeams(self):
        return self._sportsTeams

    def __repr__(self):
        string1 = f"{self.name} has the following sports teams: "
        string2 = ", ".join(self.sportsTeams)
        return ((f"{string1} {string2}").title())


if __name__ == "__main__":
    print(f"\nTesting class School\n")
    s1 = School('White Horse', 'primary', 96)
    print(s1)
    s1.numberOfStudents = 13

    print(f"\nTesting class Primary\n")
    p1 = Primary('Primary 1', 'primary', 64)
    print(p1)
    p1.numberOfStudents = 69
    print(p1)

    print(f"\nTesting class Middle\n")
    m1 = Middle('Middle 1', 'middle', 74)
    print(m1)
    m1.numberOfStudents = 86

    print(f"\nTesting class High\n")
    h1 = High('High 1', 'high', 49, ['basketball', 'tennis'])
    print(h1)
    h1.numberOfStudents = 61
    print(h1)
