
class Person:

    def __init__(self, __name, age):
        self.__name = __name
        self.age = age
        
    def __hello():
        print('Hello I an a private method')

p1 = Person('PrivateAttibute', 22)
p1.__hello()
print(p1.__name, p1.age)


class Student:
    def __init__(self, __name):
        self.__name = __name

    def getName(self):
        print(self.__name)

s1 = Student('Hi')
s1.getName()

