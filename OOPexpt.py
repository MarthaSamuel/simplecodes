#experimenting with Object Orienting Programming
#defining our first class called apple
class Apple:
    pass
#we define 2 attributes of the class and initialize as strings
class Apple:
    color = ''
    flavor = ''
# we define an instance of the apple class(object)
jonagold = Apple()
# attributes of the object
jonagold.color = 'red'
jonagold.flavor = 'sweet'
print(jonagold.color.upper())
# another instance
golden = Apple()
golden.color ='yellow'
golden.flavor = 'soft'




# this prints a poem
class Flower:
    pass
rose = Flower()
rose.color = 'red'
violet = Flower()
violet.color= 'blue'
pun = 'This pun is for you'
print('Roses are {}'.format(rose.color))
print('Violets are {}'.format(violet.color))
print(pun)




#sample 3
class Furniture:
    color = ''
    material = ''

table = Furniture()
table.color = 'brown'
table.material = 'wood'

couch = Furniture()
couch.color = 'red'
couch.material = 'leather'


def describe_furniture(piece):
    return ('This piece of furniture is made of {} {}'.format(piece.color, piece.material))
print(describe_furniture(table))
print(describe_furniture(couch))
dir(" ")
help({})
help(Apple)
