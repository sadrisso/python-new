
previousNumber = 0
presentNumber = 1
for i in range(10):
    print(previousNumber, end = ' ')
    result = previousNumber + presentNumber
    previousNumber = presentNumber
    presentNumber = result