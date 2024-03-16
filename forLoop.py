string = "Hello World"
for character in string:
    print(character)

bag = ["alu", "piyaj", "morich", 99, 0.8, 2.50, 100]
for item in bag:
    print(item)

numbers = [1,2,3,7,8,44,9,10]
for number in numbers:
    if number >= 10:
        print(number)

for i in range(1, 21):
    if i%3 == 0 and i%5 == 0:
        print(i)

sum = 0
for i in range(1,11):
    sum += i
    print(sum)