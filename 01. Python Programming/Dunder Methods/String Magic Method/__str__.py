class Name():
    def __init__(self, name):
        self.name=name
    
    def __str__(self):
        return f"MyName:{self.name}"
    
name = Name("Sayem")
print(name) # MyName:Sayem