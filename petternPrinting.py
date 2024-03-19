
for i in range(3):
    for j in range(i+1):
        print('#', end = ' ')
    print()


for row in range(10):
    for col in range(row+1):
        print('*', end = ' ')
    print()


for m in range(1, 10):
    for n in range(m):
        print('1', end = ' ')
    print()


for c in range(1, 10):
    for d in range(c):
        print(chr(64+c), end = ' ')
    print()