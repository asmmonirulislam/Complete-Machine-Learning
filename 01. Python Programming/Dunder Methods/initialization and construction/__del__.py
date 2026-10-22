# __del__ is a destructor method which is called as soon as all references of the object are deleted


# Python program to demonstrate
# __del__


class Example: 
  
    # Initializing
    def __init__(self): 
        print("Example Instance.")

    # Calling destructor
    def __del__(self): 
        print("Destructor called, Example deleted.") 
  
obj = Example() 
del obj

# Output:
# Example Instance.
# Destructor called, Example deleted.