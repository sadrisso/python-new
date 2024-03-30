
studentDetails = {
    'name' : 'mominul',
    'subjects' : ['python', 'c', 'java'],
    'topics' : ('dict', 'tuple', 'list'),
    'age' : 19,
    'gpa' : 3.99,
    'home' : 'dhaka',
    12 : 23.4,
}

studentDetails['name'] = 'hi'
print(studentDetails)
print(studentDetails['name'])
print(studentDetails[12])


# nested distionary 

nestedDict = {
    'name' : 'nested',
    'subjects' : {
        'name' : 'python',
        'age' : 123,
        'rating' : 9.8
    },
    'class' : 10
}

print(nestedDict['subjects']['rating'])

print(nestedDict.keys())
print(nestedDict.items())
print(nestedDict.pop('class'))
print(nestedDict.values())



student = {
    'roll' : 1,
    'section' : 'b'
}

newStudent = {'sub' : 'math', 'gpa' : 2.44}
student.update(newStudent)

print(student)

demoDict = {
    'cat' : 'a small and cute animal',
    'table' : ('a pice of furniture','list of facts and figure')
}
print(demoDict)


mrk1 = int(input('Enter 1st sub mark: '))
mrk2 = int(input('Enter 2nd sub mark: '))
mrk3 = int(input('Enter 3rd sub mark: '))

allSubs = {}
allSubs.update({'sub1' : mrk1})
allSubs.update({'sub2' : mrk2})
allSubs.update({'sub3' : mrk3})
print(allSubs)

# sets in python

collection = {1,2,3,3,'hello','pyhton','hello'}
print(type(collection), collection)

print(len(collection))

# empty sets; syntax

collec = set()
collec.add((1,2,3,4,5,66,66,66))
collec.add(1000)
print(type(collec), collec)


set1 = {1,2,3,4,5}
set2 = {2,3,4,5,7,8}
print(set1.union(set2))
print(set1.intersection(set2))


subjects = {'java', 'python', 'c++', 'js', 'python', 'js', 'c', 'c', 'php'}
print(len(subjects))


set = {1, 1.0}
print(set)


newSet = {
    ('float', 1.0),
    ('int', 1)
}
print(newSet)


