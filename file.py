
file = open('demo.py', 'r')
data = file.read()
print(data)
print(type(data))
file.close()


f = open('forLoop.py', 'r')
line1 = f.readline()
print(line1)
f.close()


x = open('x.txt', 'r+')
m = x.read()
y = x.write('Hi')
print(m)
print(y)
x.close()


m = open('sample.txt', 'a+')
appendElement = m.write('I am append')
readAppend = m.read()
print(appendElement)
print(readAppend)