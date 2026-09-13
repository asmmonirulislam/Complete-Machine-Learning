# *args = allows you to pass multiple non-key arguments

def add(a, b):
    print(a+b)
    
add(1,2)    # output: 3
# add(1,2,4)  TypeError: add() takes 2 positional arguments but 3 were given

def total(*args):
    print(type(args))   
    print(sum(args))    

total(1,2,3,4)  # Output:  <class 'tuple'>  10

def show_name(*args):
    for arg in args:
        print(arg, end=" ")
show_name("Sayem", "Hafiza", "Monirul")     # Output: Sayem Hafiza Monirul 