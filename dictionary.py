person = {
    'first_name' : 'Favour',
    'age' : 250,
    'married' : False,
    'skills' : ['JavaScript', 'React', 'NextJS'],
    'address' : {
        'street' : 'under-G',
        'state' : 'Oyo'
    }
}

# printing the length
print(len(person))

# to print a value from the dictionary using the key
print(person['first_name'])
# note you cannot say person['Favour']

# dictionaries can be modified
person['first_name'] = 'Favour Tochukwu'
print(person)


# .pop(key) - removes the key alongside it's values
person.pop('first_name')
print(person)

# popitem() - removes last item
person.popitem()
print(person)
