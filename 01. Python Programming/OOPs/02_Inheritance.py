# class Parent():
#     pass

# class Child(Parent):
#     pass

class User():
    def __init__(self, id, name, contact, address):
        self.id=id
        self.name=name
        self.contact=contact
        self.address=address
        
class Employee(User):
    def __init__(self, id, name, contact, address, role, dept):
        super().__init__(id, name, contact, address)
        self.role=role
        self.dept=dept
    def getInfo(self):
        print(f"{self.name}, {self.id}, {self.contact}, {self.address}, {self.role}, {self.dept}")
    
sayem = Employee(3982, None, "01401411046", "Mirpur, Dhaka", "SDE", "CSE")
sayem.getInfo()