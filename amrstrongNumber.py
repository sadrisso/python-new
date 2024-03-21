
a = input('Enter a number: ')
num_len = len(a)
sum = 0
for i in a:
    sum += int(i)**num_len

if int(a) == sum:
    print('Armstrong number')
else:
    print('Not armstrong number')