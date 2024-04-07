
# class Complex:

#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def show_number(self):
#         print(self.real,'i +', self.img,'j')

#     def add(self, n2):
#         newReal = self.real + n2.real
#         newImg = self.img + n2.img
#         return Complex(newReal, newImg)

# n1 = Complex(1, 3)
# n1.show_number()

# n2 = Complex(2, 5)
# n2.show_number()

# n3 = n1.add(n2)
# n3.show_number()

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, 'i -', self.img, 'j')

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(4, 8)
num2 = Complex(3, 7)
num1.showNum()
num2.showNum()
# num3 = num1.sub(num2)
num3 = num1 - num2
num3.showNum()