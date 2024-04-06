# Create a student class that takes name and marks of three subjects as argument in constructor.
# Then create a method to print the average


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def calculate_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('Hi', self.name, 'your avg score is: ', sum/3)

s1 = Student('Miraz', [80, 78, 98])
s1.calculate_average()



