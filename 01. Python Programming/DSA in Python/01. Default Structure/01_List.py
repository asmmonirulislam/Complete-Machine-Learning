"""
List works like a Stack

li = []

li.append(1) : [1]
li.append(2) : [1, 2]
li.append(3) : [1, 2, 3]

li.pop() : [1, 2] -> 3 pops from the end
li.pop() : [1] -> 2 pops from the end
li.pop() : [] -> 1 pops from the end

"""



l1 = ['Monirul', 'Sayem', 3982, 39.82, True, None, False]
l2 = [7, 1, 5, 2, 8, 9, 3, 4, 6]

print(l1[0])    #Monirul
print(l1[0][6]) #l

#   append() - adds elements at the end of the list
l1.append('NewElement')
l1.append('anotherElement')
print(l1)   #   ['Monirul', 'Sayem', 3982, 39.82, True, None, False, 'NewElement', 'anotherElement']

####   pop() - pops element from the end
print(l1.pop()) # anotherElement

#   sort() - sorts the list in ascending order
l2.sort()
print(l2)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#   reverse() - reverse the list
l1.reverse()
print(l1)   # ['NewElement', False, None, True, 39.82, 3982, 'Sayem', 'Monirul']

#   insert(x, y) - inserts y at x index
l1.insert(3, 'Hafiza')
print(l1)   # ['NewElement', False, None, 'Hafiza', True, 39.82, 3982, 'Sayem', 'Monirul']

#   pop(x) - deletes elements from x index and returns its value
print(l1.pop(3)) # Hafiza
print(l1) # ['NewElement', False, None, True, 39.82, 3982, 'Sayem', 'Monirul']

#   remove(x) - removes x from the list
l1.remove('NewElement')
print(l1)   #[False, None, True, 39.82, 3982, 'Sayem', 'Monirul']

#   sum() - calculates the sum of the list
print(sum(l2)) # 45

#   count(x) - returns the occurence of x
print(l2.count(5)) # 1

#   max() - returns the max element
print(max(l2))

#   min() - returns the min element
print(min(l2))  # 1