class Employee():
    def __init__(self):
        self.id = None
        # Write your code
        self._id = 'Whacked'  # use for variable accessible to module
        self.__id = "Smacked"  # use for variable accessible to class only


e = Employee()
print(dir(e))
