# A lambda function is a small anoynymous function
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax: lambda arguments, expression

add = lambda a, b : a+b
print(add(5, 6)) # 11

# similar to the function:

def add2(a:int, b:int)->int:
    return a+b
print(add2(5, 6))  # 11