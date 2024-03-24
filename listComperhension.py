
# it return string formate list

a = input().split()
print(a)


# it return integer formate list

b = list(map(int, input().split()))
print(b)


c = list(map(float, input().split()))
print(c)


# iteration with list comprehension

x = [10, 20, 30, 40]
y = [i*2 for i in x]
print(y)

c = [10, 20, 40, 90]
d = [i+5 for i in c]
print(d)

e = [1, 2, 3,4,5]
f = [i-1 for i in e]
print(f)