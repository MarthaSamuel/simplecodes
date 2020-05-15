# Author: Dimgba Martha O
# @martha_samuel_
# 01 this code samples the use of definition
name = 'Martha'
print(type(name))
print('Hello! ' + name)


# using definitions
def greeting(person):
    print('Welcome ' + person)


greeting('Martha')


def greeting(person, department):
    print('Welcome! ' + person)
    print('You are part of ' + department)


greeting('Martha', 'IT Support')
