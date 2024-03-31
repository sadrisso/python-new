
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
    for i in numbers:
        sum += i
        avg = sum/len(numbers)
        print(avg)

getAvg(3,7,10,40)


# tuple basic

tup = (1,222,3,4,5,6, 'red', True, False, 'Hi', 334)
print(type(tup), tup)
print(tup[0])
print(tup[-1])

if 22 in tup:
    print('Yes 22 is present in', tup)
else:
    print('No 22 ' + 'Check', tup)

tup2 = tup[1:4]
print('Tuple 2 is here', tup2)



def myFunction(you, me):
    if you and me == 'love':
        print('we are in love')
    if you == 'love':
        print('half love')
    if you and me == 'hate':
        print('devorce')

myFunction('love', 'hate')



def printList(list):
    for item in list:
        print(item, end = ' ')

printList([1,2,3,4,54,5,6,67,78,544])


# factorial fiding function


def findFactorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)

findFactorial(5)
findFactorial(6)
findFactorial(7)



# usd to bdt function 

def calc_bdt(usd):
    bdt = usd*100
    print(usd,'USD = ', bdt,'BDT')

calc_bdt(8)


# even odd print

def even_or_odd(num):
    if num % 2 == 0:
        print(num, '=', 'Even')
    else:
        print(num, '=', 'Odd')

even_or_odd(32)