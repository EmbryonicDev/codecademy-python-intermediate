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


class Middle(School):
    def __init__(self, name, numberOfStudents, level='primary'):
        School.__init__(self, name, numberOfStudents, level)


class High(School):
    def __init__(self, name, numberOfStudents, level='primary', *sportsTeams):
        School.__init__(self, name, numberOfStudents, level)
        self._sportsTeams = list(sportsTeams)[0]

    @property
    def sportsTeams(self):
        string1 = f"{self.name} has the following sports teams: "
        string2 = ", ".join(self._sportsTeams)
        return ((f"{string1} {string2}").title())


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

    print(f"\nTesting class Middle\n")
    m1 = Middle('Middle 1', 74, 'middle')
    print(m1)
    m1.numberOfStudents = 86

    print(f"\nTesting class High\n")
    h1 = High('High 1', 49, 'high', ['basketball', 'tennis'])
    print(h1)
    h1.numberOfStudents = 61
    print(h1.sportsTeams)
