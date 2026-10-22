# __new__ : Responsible for creating a new instance of the class.


class A:
    def __new__(cls):
        print("Creating instance")

    def __init__(self):
        print("Initializing instance")

a = A()

#Output: Creating instance