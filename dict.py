
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