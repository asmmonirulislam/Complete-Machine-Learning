t1 = ()
print(type(t1))    # <class 'tuple'> 

t2 = (1)
print(type(t2)) # <class 'int'>

t3 = (1,)
print(type(t3)) # <class 'tuple'>

t4 = (5,3,1,2,4)

t5 = ("monirul", 45, 342, False, "sayem", 45)

# Methods

#01. count(x) - number of x in the tupple
print(t5.count(45)) # 2

#02. index(x) - returns the index of the first occurence of x
print(t5.index(False)) # 3

#03. len(t) - length of the tupple
print(len(t5)) # 6

#04. max(t) - maximum value of the tupple
print(max(t4)) # 5

# 05. min(t) - minimum value of tupple
print(min(t4)) # 1

# 06. sum(t) - sum of the elements
print(sum(t4))  # 15

# 07. sorted(t) - sort the tupple(doesn't modify)
print(sorted(t4))   # [1, 2, 3, 4, 5]

# 08. tuple(iterable) - converts an iterable into a tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple) #(1, 2, 3, 4, 5)

# 09. in, not in - membeship check
print(45 in t5) #True

# 10. tuple slicing
print(t5[1:3])  # (45, 342)

# 11. concatenation
t6 = (1, 2)
t7 = (3, 4)
print(t6+t7) # (1, 2, 3, 4)

# 12. repetition
print(t6*3) # (1, 2, 1, 2, 1, 2)

# 13. tupple unpacking
x, y = t6
print(x, y) # 1 2

# 14. nested tuple
nested = (
    ("Monirul",2),
    ("Sayem",4)
)
print(nested) # (('Monirul', 2), ('Sayem', 4))

for x, y in nested:
    if x=='Monirul':
        print(y)
        break
# Output: 2