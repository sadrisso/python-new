
# transpose matrix conversion

matrix = [[1,2], [3,4], [4,5], [5,6]]
 
a = []                                  # with for loop
for row in range(2):                    # outer loop
    b = []
    for col in matrix:                  # inner loop
        b.append(col[row])
    a.append(b)
print(a)


# with list comprehension

res = [[col[row] for col in matrix] for row in range(2)]
print(res)


# swaping a list element

list1 = [1,2,3,4,5,6,7,8,9]
temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp
print(list1)


# count unique element in a list

m = [1,2,2,3,3,3,4,5,6]
n = []
count = 0
for i in m:
    if i not in n:
        n.append(i)
        count += 1
print(count)


# extract element from a list

testList = [1,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,6,6]
k = 3
x = []
for i in testList:
    freq = testList.count(i)
    if freq > k and i not in x:
        x.append(i)
print(x)


myList = [1,1,1,1,3,3,3,3,5,5,5,5,66,66,77,77,78]
element = 3
y = []
for i in myList:
    f = myList.count(i)
    if f > element and i not in y:
        y.append(i)
print(y)
