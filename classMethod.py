
class Person:
    name = 'Arham'

    @classmethod
    def changeName(cls, name):
        cls.name = name
        print(name)

p1 = Person()
p1.changeName('Ratul')
print(Person.name)


# property method

class Student:
    def __init__(self, phy, chm, math):
        self.phy = phy
        self.chm = chm
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy + self.chm + self.math) / 3) + '%'

s1 = Student(98, 99, 89)
s1.phy = 88
print(s1.percentage)




