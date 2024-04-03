
file = open('demo.py', 'r')
data = file.read()
print(data)
print(type(data))
file.close()

f = open('forLoop.py', 'r')
line1 = f.readline()
print(line1)
f.close()