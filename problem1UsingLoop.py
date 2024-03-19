
a = int(input('Enter a number: '))
for i in range(1, a+1):
    print(a, 'X', i, '=', a*i)


b = int(input('Enter your number: '))
for i in range(1, 10):
    print(b, 'X', i, '=', b*i)


c = int(input('Enter a number: '))
factorial = 1
for i in range(1, c+1):
    factorial = factorial*i
print(factorial)