
# movies = []
# movies.append(input('Enter the first movie: '))
# movies.append(input('Enter the 2nd movie: '))
# movies.append(input('Enter the 3rd movie: '))

# print(movies)


# palindrom check

x = [1,2,3,3,2,1]
copyOfx = x.copy()
copyOfx.reverse()

if copyOfx == x:
    print('palindrom')
else:
    print('not palindrom')


studentTuple = ('d', 'a', 'a', 'b', 'a', 'd', 'a', 'c')
print(studentTuple.count('a'))



gradeList = ['d', 'a', 'a', 'b', 'a', 'd', 'a', 'c']
print(gradeList.sort(), gradeList)
