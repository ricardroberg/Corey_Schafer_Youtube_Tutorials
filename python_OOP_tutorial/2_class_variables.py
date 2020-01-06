
class Employee:
    # Variáveis de classe se aplicam a todas as instâncias.
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Variáveis de instância. Únicas para cada instância.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        # self.pay = int(self.pay * Employee.raise_amount)  # Aplicando a variável de classe
        self.pay = int(self.pay * self.raise_amount)  # Aplicando a variável de classe que está definida para a instância


print(Employee.num_of_emps)  # 0

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(Employee.num_of_emps)  # 2

# print(emp_1.__dict__)
# {'first': 'Corey', 'last': 'Schafer', 'pay': 50000, 'email': 'Corey.Schafer@company.com'}

# Employee.raise_amount = 1.05  # Define para toda a classe
# emp_1.raise_amount = 1.05  # Define somente para a instância

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

