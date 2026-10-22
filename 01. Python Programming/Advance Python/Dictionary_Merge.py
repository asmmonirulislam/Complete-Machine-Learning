# New operators | and |= allow for merging and updating dictionaries.

dict1 = {
    'a':1,
    'b':2
}

dict2 = {
    'c':3,
    'd':4
}

dict3 = dict1 | dict2

print(dict1) #{'a': 1, 'b': 2}
print(dict2) #{'c': 3, 'd': 4}
print(dict3) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict1 |= dict2

print(dict1) #{'a': 1, 'b': 2, 'c': 3, 'd': 4}