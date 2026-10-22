# __init__() method is a constructor which is automatically called when a new object of a class is created. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person("Max", 30)
b = Person("Emilia", 25)

print(a.name, a.age) 
print(b.name, b.age)

# Output:
# Max 30
# Emilia 25