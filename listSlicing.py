
# list = [11, 54, 6765, 3.4, 'Mango', 'Banana']

# print(list[::])
# print(list[1:3:1])
# print(list[-1:-4:-1])
# print(list[::-1])


x = [11, 43, 77, 4.5, 'Ami', 'Tmi', 'Sobai']
y = [22, 54, 4, 'Mango', 'Lichi']
z = x+y
print(z)

m = 'Mango'
print(list(m))

a = ['Rahim', 'Karim', 'Shakib', 'Mominul', 'Sabbir']
a.append('Shoumya')
print(a)

a.insert(0, 'Rakib')
print(a)

b = a.copy()
print(b)

print(x.count(11))

a.extend(['Miraj', 'Mahmudullah', 'Mahmudul', 'Munim'])
print(a)
a+=['Miraj', 'Mahmudullah']
print(a)


m = [1,2,3,45,6]

print(m.pop())
print(m)

m.remove(m[3])
print(m)

n = [1,2,3,4,5]
# n.clear()
print(n)

# print(n[::-1])
n.reverse()
print(n)

n.sort()
print(n)
n.sort(reverse = True)
print(n)


p = [1,2,34,5,676,4,322,111]
print(max(p))
print(min(p))