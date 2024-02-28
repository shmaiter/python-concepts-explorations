# Corey Schafer
class Employee:
    
    num_of_emp = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emp += 1
    
    # Regular instance method
    def fullname(self):
        return f'{self.first} {self.last}'
    
    # instance methods pass the instance(self) as first argument
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # classmethods pass the class(cls) as first argument
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    # classmethods as alternative constructors
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # if you don't need to access the instance nor the class, is better
    # to use a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')
            
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Shmaiter', 'Morales', 57400, 'Java')

mang_1 = Manager('Alexa', 'Medina', 75000, [dev_1])

