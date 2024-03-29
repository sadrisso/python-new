
def calculateMean(a, b):
    mean = (a+b)/2
    print(mean)

calculateMean(2,2)
calculateMean(5,5)


def calculateGmean(c, d):
    gmean = (c*d)/(c+d)
    print(gmean)

calculateGmean(2,3)


def even_number_check(e):
    if e%2 == 0:
        print('Even number')
    else:
        print('Odd number')

even_number_check(2)


def bigNumber(m, n):
    if m>n:
        print(m,'is greter then', n)
    else:
        print('Default')

bigNumber(223,34)


def isLesser(w,x):
    pass


# default arguments in function

def calculateAverage(x = 10, y = 20):
    print('Average is', (x+y)/2)

calculateAverage(20)



# function for getting average

def getAvg(*numbers):
    sum = 0
    count = 0
    for i in numbers:
        count += 1
        sum += i
        avg = sum/count
        print(avg)

getAvg(3,7,10,40,50)
    