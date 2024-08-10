fruits = ['banana', 'orange', 'mango', 'lemon', 'cola']

all_fruits = fruits[0:4]
skip = fruits[::2]
reverse_order = fruits[::-1]

print(skip)
print(reverse_order)

# to replace an item on list,yake avocado for example
fruits[0] = 'avocado'
print(fruits)

# to find something in a list
orange = 'orange' in fruits
pawpaw = 'pawpaw' in fruits

print(orange)
print(pawpaw)

# Adding items to the list
fruits.append('stone')
print(fruits)

#insert items at specific index
fruits.insert(2, 'apple')
fruits.insert(3, 'lime')
print(fruits)


# removing items
fruits.remove('apple')
fruits.remove('lime')
print(fruits)

# removing last item with pop
fruits.pop()
print(fruits)

# deleting items
del fruits[0]
print(fruits)

del fruits[0:2]
print(fruits)

# sorting items in a list
# in ascending order
fruits.sort
print(fruits)

# in descending order
fruits.sort(reverse=True)
print(fruits)