
class Student:
    
    name = 'Karan Sharma'
    age = 12
    section = 'A'

s1 = Student()
print(s1.name, s1.age, s1.section)

s2 = Student()
print(s2.name, s2.age, s2.section)


class Teacher:

    collegeName = 'ABC College'
    name = 'Arjun' # class attribute
    
    # default constructor
    def __init__(self):
        pass

    # peramitarized constructor
    def __init__(self, name, rank, sallary):
        self.name = name # object attibute
        self.rank = rank
        self.sallary = sallary
        print('adding new student in database: ')
        
t1 = Teacher('Ajij', 'B', 20000)
print(t1.name, t1.rank, t1.sallary)

t2 = Teacher('Amin', 'A', 30000)
print(t2.name, t2.rank, t2.sallary)



class Person:

    matches = 45  # class attribute
    name = 'anonimous'

    def __init__(self, name, age):
        self.name = name  # object attribute
        self.age = age


p1 = Person('Mushfiq', 40)
p2 = Person('Shakib', 37)
p3 = Person('Mahmudullah', 50)

print(p1.name, p1.age, p1.matches)
print(p2.name, p2.age, p2.matches)
print(p3.name, p3.age, p3.matches)


class Player1:

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def welcome(self):
        print('Welcome', self.name)

    def get_skill(self):
        print(self.skill)


p1 = Player1('Shakib Al Hasan', 'All-Rounder')
p1.welcome()
p1.get_skill()
