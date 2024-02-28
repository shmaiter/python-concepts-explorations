class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        classname = type(self).__name__
        return f'{classname}({self.name}, {self.age}, {self.salary})'

emp1 = Employee("Sarah", 34, 456000)
emp2 = Employee("Mica", 29, 850000)
emp3 = Employee("Meri", 54, 490000)

empl_list = [emp1, emp2, emp3]

# method 1
def sort_obj(emp):
    return emp.name

print(sorted(empl_list, key=sort_obj))