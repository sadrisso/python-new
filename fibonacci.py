
previousNumber = 0
presentNumber = 1

for i in range(10):
    print(previousNumber, end = ' ')
    result = previousNumber + presentNumber
    previousNumber = presentNumber
    presentNumber = result


m = 0
n = 1

for f in range(10):
    print(m, end = ' ')
    sum = m + n
    m = n
    n = sum


k = 1
for j in range(10):
    print(j, end = ' ')
    addition = j+k
    j = k
    k = addition 


a = int(input('Enter a digit: '))

count = 0
while a>0:
    a = a//10
    count = count + 1
print(count)