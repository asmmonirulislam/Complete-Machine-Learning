print(abs(-10)) #10

class Number():
    def __init__(self, num):
        self.num=num
        
    def __abs__(self):
        return abs(self.num)
    
num = Number(-13)
print(abs(num)) #13