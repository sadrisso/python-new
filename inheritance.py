# class Car:
#     @staticmethod
#     def start():
#         print('Car started..')

#     @staticmethod
#     def stop():
#         print('Car stoped.')

# class TeslaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = TeslaCar('Tcs')
# print(car1.name, car1.start(), car1.stop())


class Bus:

    @staticmethod
    def start():
        print('Bus started ...')

    @staticmethod
    def stop():
        print('Bus stoped.')

class Hanif(Bus):

    def __init__(self, type):
        self.type = type


class Type(Hanif):

    def __init__(self, fuel):
        self.fuel = fuel


type1 = Type('diesel')
bus1 = Hanif('Hino')
type1.start()
print(bus1.type)
print(type1.fuel)


# Multiple inheritance
class A:
    def welcome(self):
        print('Welcome from class A')

class B:
    def hello(self):
        print('Hello, welcome from class B')

class C(A, B):
    def __init__(self, name):
        self.name = name

c1 = C('himalaya')
c1.welcome()
c1.hello()