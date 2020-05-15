# experimenting with constructors(--init__) called when you call the name of the class
#methods with __  __ are special methods
class Apple:
    def __init__(self,color,flavor):
        '''Initialize the instance attribute to the attribute in the parameter'''
        self.color =color
        self.flavor=flavor
jonagold= Apple('red','sweet')
print(jonagold.color)

class Person():
    def __init__(self,name):
        self.name=name
    def greeting(self):
        return 'Hi, my name is ' + self.name
some_person=Person('John')
print(some_person.greeting())
'''if the method is not printed,it prints the location where instance is stored in the computer memory'''
print(some_person)


'''we use the str method to return the string we want to print'''
def __str__(self):


