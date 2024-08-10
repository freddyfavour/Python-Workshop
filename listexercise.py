heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# printing the length
print(len(heros))

# add black panther
heros.append('black panther')
print(heros)

# remove black panther and replace hulk with black panther
heros.remove('black panther')
heros[2] = 'black panther'
print(heros)
