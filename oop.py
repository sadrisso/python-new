
class Student:
    name = 'Karan Sharma'
    age = 12
    section = 'A'

s1 = Student()
print(s1.name, s1.age, s1.section)

s2 = Student()
print(s2.name, s2.age, s2.section)


class Teacher:
    def __init__(self, name, rank, sallary):
        self.name = name
        self.rank = rank
        self.sallary = sallary
        print('adding new student in database: ')
        
t1 = Teacher('Ajij', 'B', 20000)
print(t1.name, t1.rank, t1.sallary)

t2 = Teacher('Amin', 'A', 30000)
print(t2.name, t2.rank, t2.sallary)