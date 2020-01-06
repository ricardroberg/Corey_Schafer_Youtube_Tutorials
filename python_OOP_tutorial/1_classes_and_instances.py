# Python Object-Oriented Programming

# Class is a blueprint

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

# Definindo usando método construtor
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

# Full Name sem criar método de classe
# print(f'{emp_1.first} {emp_1.last}')
print(emp_1.fullname())

print(Employee.fullname(emp_1))

# print(emp_1)
# print(emp_2)

# Definindo atributos de instancia manualmente
# emp_1 = Employee()
# emp_2 = Employee()
#
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000



