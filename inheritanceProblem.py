class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print('Role =', self.role)
        print('dept =', self.dept)
        print('salary =', self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__('computer', 'IT', 50000)

    def show_details(self):
        print('Name =', self.name)
        print('Age =',  26)
        super().show_details()

e1 = Employee('Accountant', 'Finance', '40000')
e1.show_details()

e2 = Engineer('Drisso', 26)
e2.show_details()
