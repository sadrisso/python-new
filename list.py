 
a = [11, 34, 21, 1.8, 'Alu', 'piyaj']
print(a[4])
print(a[0])
a[0] = 'changed'
print(a[0])



b = [11, 23, 45.5, 'Ami', 'tmi']
print(b[-3])
print(b[-1])
print(b[4])



b[-3] = 500 # changed in memory
if 45.5 in b:
    print('Found')
else:
    print('Not found')



# negetive index printing 
    
for i in range(len(b)-1, -1, -1):
    print(b[i])

for i in range(-1, -len(b)-1, -1):
    print(b[i])