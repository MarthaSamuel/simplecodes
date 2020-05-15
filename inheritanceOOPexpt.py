# experimenting with inheritance
class Fruits:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
class Apple(Fruits):
    pass
class Grape(Fruits):
    pass
jonagold=Apple('green','tart')
carn=Grape(' blue','sweet')
print(jonagold.flavor)


#sample 2
class Animal:
    sound =''
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('{sound} i`m {name}'.format(name=self.name,sound=self.sound))
class Piglet(Animal):
    sound='oink!'
hamlet=Piglet('Hamlet')
hamlet.speak()
class Cow(Animal):
    sound ='moo'
milky=Cow('Milky')
milky.speak()



#sample3
class Clothing:
    material=''
    '''in constructor,injtialize the parameters'''
    def __init__(self,name):
        self.name=name
    def checkmaterial(self):
        print('this {} is made of {}'.format(self.name, self.material))
class Shirt(Clothing):
    material='cotton'
polo=Shirt('Polo')
polo.checkmaterial()




