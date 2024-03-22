
a = input('Enter a number: ')
num_len = len(a)
sum = 0
for i in a:
    sum += int(i)**num_len

if int(a) == sum:
    print('Armstrong number')
else:
    print('Not armstrong number')



m = int(input('Enter a number: '))
rev_a = 0

while m>0:
    last_digit = m%10
    rev_a = rev_a * 10 + last_digit
    m //= 10
print(rev_a)