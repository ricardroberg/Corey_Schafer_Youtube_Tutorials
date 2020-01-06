# Python OPP
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount  # Altera a variável de classe

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

"""
Quando trabalhamos com classes, métodos regulares automaticamente passam a instância como primeiro argumento(self)
QUando trabalhamos com métodos de classe (@classmethod) é passado a classe como primeiro argmento(cls)
Métodos estáticos (@staticmethod) não passam nada automaticamente como primeiro argumento.
"""

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2020, 1, 6)
my_date2 = datetime.date(2020, 1, 5)

print(Employee.is_workday(my_date))
print(emp_2.is_workday(my_date2))

# CLASS METHOD
# emp_1.raise_amt = 1.06
# Employee.set_raise_amt(1.05)  # Altera para a classe e toda instância que não teve o valor definido manualmente
# emp_2.set_raise_amt(1.03)  # Mesmo utilizando a instância ele vai alterar tudo, pois é um método de classe
#
#
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
