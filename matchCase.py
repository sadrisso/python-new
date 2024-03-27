
matchVariable = int(input('Enter the value you want to match: '))

match matchVariable:
    case _ if matchVariable >= 100:
        print(matchVariable, 'is greter then 100')
    case _ if matchVariable % 2 == 0:
        print(matchVariable, 'is an even number')
    case _ if matchVariable % 3 == 0:
        print(matchVariable, 'is an odd number')
    case _ :
        print(matchVariable, 'is a default number')
        