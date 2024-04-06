class Car:
    @staticmethod
    def start():
        print('Car started..')

    @staticmethod
    def stop():
        print('Car stoped.')

class TeslaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TeslaCar('Tcs')
print(car1.name, car1.start(), car1.stop())