
# transpose matrix conversion

matrix = [[1,2], [3,4], [4,5], [5,6]]
 
 
# with for loop

a = []
for row in range(2): # outer loop
    b = []
    for col in matrix: # inner loop
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