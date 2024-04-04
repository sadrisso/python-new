
file = open('demo.py', 'r')
data = file.read()
print(data)
print(type(data))
file.close()


f = open('forLoop.py', 'r')
line1 = f.readline()
print(line1)
f.close()


# x = open('x.txt', 'r+')
# m = x.read()
# y = x.write('Hi')
# print(m)
# print(y)
# x.close()


m = open('sample.txt', 'a+')
appendElement = m.write('I am append')
readAppend = m.read()
print(appendElement)
print(readAppend)


with open('sample.txt', 'r') as fi:
    fData = fi.read()
    print(fData)

with open('sample.txt', 'w') as fi:
    fData = fi.write('This is new text')

# import os
# os.remove('x.txt')

with open('practice.txt', 'w') as filee:
    print(filee.write('Hi i am learning java, I love to write java programe'))


with open('practice.txt', 'r') as filee:
    data = filee.read()
    new_data = data.replace('java', 'python')
    print(new_data)

with open('practice.txt', 'w') as filee:
    filee.write(new_data)


def check_for_word():
    word = 'learning'
    with open('practice.txt', 'r') as filee:
        ddata = filee.read()
        if word in ddata:
            print('Found')
        else:
            print('Not found')

check_for_word()

def check_for_line():
    word = 'learning'
    data = True
    line_no = 1
    while data:
        with open('practice.txt', 'r') as filee:
            data = filee.readline()
            if word in data:
                print(line_no)
                line_no += 1
                return
        return -1
    
check_for_line()

with open('practice.txt', 'w') as filee:
    nums = filee.write('1,2,3,34,6,75,3,231,1,11')
    print(nums)

with open('practice.txt', 'r') as filee:
    data = filee.read()
    
    # num = ''
    # for i in range(len(data)):
    #     if data[i] == ',':
    #         print(int(num))
    #         num = ''
    #     else:
    #         num += data[i]
    
    count = 0
    nums = data.split(',')
    for val in nums:
        if int(val) %2 == 0:
            count += 1

    print(count)  

