# ways to create a new list
#x = list()
#x = ['a', '25', 'cat']
#x = list(tuple)
# list and some of its methods
fruits = ['apple', 'pineapple', 'cherry', 'carrot']
print(type(fruits))
print(fruits)
print(len(fruits))
#checking membership
print('apple' in fruits)
print('car' in fruits)
#indexing and slicing
print(fruits[0])
print(fruits[:-2])
print(fruits[1:])
print(fruits.index('carrot'))
# adding elements to list
fruits.append('mango')
print(fruits)
fruits.extend(['berry', 'pear', 'banana'])
print(fruits)
fruits.insert(2, 'pawpaw')
print(fruits)
fruits.insert(90, 'soursop')
print(fruits)
#assigning elements. removes former element
fruits[0] = 'cashew'
print(fruits)
# removing an element
print(fruits.pop(3))
print(fruits)
fruits.remove('pear')
print(fruits)
del fruits[-2:]
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.count('mango'))
fruits.append('apples')
print(fruits)
print(sorted(fruits))
for index,item in enumerate(fruits):
    print(index,item)
for index,item in enumerate(fruits, start=1):
    print(index,item)
print(fruits)
print(reversed(fruits))







