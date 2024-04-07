import random

randomNumber = random.randint(1,50)

while True:
    userChoice = input('Enter your guess from 1 - 50 or OUIT(Q): ')
    if userChoice == 'Q':
        break
    userChoice = int(userChoice)
    if userChoice == randomNumber:
        print('You win, Congratulations')
        break
    elif(userChoice > randomNumber):
        print('Please choose smaller number, Your number is too big')
    else:
        print('Please choose bigger number, Your number is too small')

print("----GAME OVER----")