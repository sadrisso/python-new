a = 0
while a <= 10:
    a = a + 1
    print(a)

x = 10
while x >= 0:
    x = x - 1
    if x == 3:
        break
    print(x)

y = 100
while y >= 0:
    y = y - 5
    print(y)
    if y == 90:
        break

for i in range(10, 21, 2):
    if i == 16:
        continue
    print(i)

z = 100
while z >= 0:
    z = z - 10
    if z == 10:
        continue
    print(z)