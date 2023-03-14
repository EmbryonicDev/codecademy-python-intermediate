class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1


class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print("ID {} added.".format(employee.id))
        self.attendees.append(employee)

    def __len__(self):
        return len(self.attendees)

    # Write your code


e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()

for x in [e1, e2, e3]:
    m1+x

print(len(m1))
