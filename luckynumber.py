# Author: Dimgba Martha O
# @martha_samuel_
# 02 sample code demonstrating the use of definition
name = 'Martha'
number = len(name) * 9
print('hello ' + name + '.Your lucky number is ' + str(number))


# using definition
def lucky_number(name):
    number = len(name)*9
    print('hello ' + name + '.Your lucky number is ' + str(number))
lucky_number('Okenwa')
lucky_number('Ibe')
