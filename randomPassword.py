import string
import random


passLen = 10

charVal = string.ascii_letters + string.digits + string.punctuation

# randomPass = ''
# for i in range(passLen):
#     randomPass += random.choice(charVal)

# print('Random Password is:', randomPass)



# list comprehension

randomPassword = ''.join([random.choice(charVal) for i in range(passLen)])
print(randomPassword)