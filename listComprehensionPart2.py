
# using if with list comprehension

a = []
for i in range(1, 20):
    if i % 3 == 0:
        a.append(i)
print(a)

m = [i for i in range(1, 20) if i % 3 == 0]
print(m)

n = [i for i in range(1, 10) if i % 2 ==0 if i % 4 == 0]
print(n)

o = ['Even' if i % 2 == 0 else 'odd' for i in range(1, 10)]
print(o)