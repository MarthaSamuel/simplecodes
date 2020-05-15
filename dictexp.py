# experimenting with dictionaries
#constructing dictionaries
# x = { : , : , : }
# x = dict([( , ), ( , ),( , )])
# x = dict(key = value, key = value)
# some dict methods and operations
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Comp Sci']}
print(student['name'])
# we use get() to call a key that dont exist so we dont get an error
print(student.get('phone'))
# to return 'Not found' instead
print(student.get('phone','Not Found'))
# to assign
student['name']='Martha'
print(student)
# to update more than one key we use update()
student.update({'age':26,'phone':'111222333', 'sex': 'female'})
print(student)
# to remove key, we can use del, pop(), or dict.clear()
del student['age']
print(student)
for key in student:
    print(key, student[key])
print(student)
print(student.values())
print(student.keys())
for key,value in student.items():
    print(key,value)
print('name' in student)
