# **kwargs = allows you to pass multiple keyword-arguments

def display_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    
display_address(Holding = "J12", Street="Road no 05", Area = "Arifabad Housing Society")
# Output:
# <class 'dict'>
# Holding = J12
# Street = Road no 05
# Area = Arifabad Housing Society
