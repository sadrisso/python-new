
class Person:
    name = 'Arham'

    @classmethod
    def changeName(cls, name):
        cls.name = name
        print(name)

p1 = Person()
p1.changeName('Ratul')
print(Person.name)
