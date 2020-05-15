#sample
class Piglet:
    pass
class Piglet:
    #we define a method of the class with def .
#the parameter is self which represents the instance of the method being executed on
    def speak(self):
        print('oink oink')
        #instance
hamlet = Piglet()
hamlet.speak()




class Piglet:
    name = 'piglet'
    def speak(self):
        print('oink i`m {}'.format(self.name))
hamlet = Piglet()
hamlet.name='Hamlet'
hamlet.speak()
pet = Piglet()
pet.name='Pet'
pet.speak()





#
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
piggy=Piglet()
print(piggy.pig_years())
piggy.years=2
print(piggy.pig_years())


class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7
fido = Dog()
fido.years=3
print(fido.dog_years())

