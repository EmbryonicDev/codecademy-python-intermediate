class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))


class Admin(Employee):
    def say_id(self):
        # Write your code below:
        super().say_id()
        print("I am an admin.")


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()
