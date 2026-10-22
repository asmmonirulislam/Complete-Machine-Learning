class User():
    def __init__(self, id=None, name=None, contact=None, address=None):
        self.id=id
        self.name=name
        self.contact=contact
        self.address=address
        
class Student(User):
    def __init__(self, dept=None, batch=None, **kwargs):
        super().__init__(**kwargs)
        
        self.dept = dept
        self.batch = batch
        
    def showDetails(self):
        # data = [self.id, self.name, self.contact, self.address, self.dept, self.batch]
        # new_data = [item for item in data if item is not None]
        # print(*new_data)
        print(*[item for item in self.__dict__.values() if item is not None])
    
sayem = Student(dept="CSE", batch="65D", name="A S M Monirul Islam", id=3982)
sayem.showDetails()