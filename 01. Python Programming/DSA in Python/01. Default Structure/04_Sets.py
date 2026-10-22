s1 = set() #empty set
print(type(s1)) #<class 'set'>

s2 = {1,5,7,2,3,4,3}
print(type(s2)) #<class 'set'>
print(s2) #{1, 2, 3, 4, 5, 7}

#PROPERTIES
# 01. SETS ARE ORDERED
# 02. SETS ARE UNINDEXED
# 03. THERE IS NO WAY TO CHANGE ITEMS IN SETS
# 04. SETS CAN NOT CONTAIN DUPLICATE 



# SETS METHODS

# 01. add() - adds elements
s1.add(1)
s1.add(3)
s1.add(2)
print(s1) #{1, 2, 3}

# 02. len(s) - size of the set
print(len(s2)) #6 (doesn't count duplicate values)
# 03. remove(x) - updates the set and removes x from the set
s2.remove(3)
print(s2) #{1, 2, 4, 5, 7}
# 04. pop() - removes the first value from the set but returns it
val = s1.pop() 
print(val) #1
print(s1) #{2, 3}
# 05. clear() - wipes the set
s1.clear()
print(s1) #set()
# 06. union({x,y,z}) - returns a new set with all items from both sets (but doesn't update)
print(s2.union({8,9,10})) #{1, 2, 4, 5, 7, 8, 9, 10}
# 07. intersection({x,y,z}) - returns a set which contains only item in both sets (but doesn't update)
print(s2.intersection({4,7,9,10})) #{4, 7}
# 08. issubset(ss) - checks the subset
s3 = {4,7}
print(s3.issubset(s2)) #True
# 09. issuperset(s) - checks the superset
print(s2.issuperset(s3)) #True