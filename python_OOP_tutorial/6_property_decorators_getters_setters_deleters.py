
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')  # fname = name.split(' ')
        self.first = first  # self.first = fname[0]
        self.last = last  # self.last = fname[-1]

    @fullname.deleter
    def fullname(self):
        print(f'Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
print(emp_1.fullname)
emp_1.fullname = 'Corey Schafer'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)