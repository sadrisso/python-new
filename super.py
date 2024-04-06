
class Student:

    def welcome(self):
        print('Welcome from student class')

class Teacher:
    
    def hiTeacher(self):
        print('Hi from teacher class')

class Person(Student, Teacher):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().welcome()
        super().hiTeacher()

p1 = Person('Hossain', 32)
