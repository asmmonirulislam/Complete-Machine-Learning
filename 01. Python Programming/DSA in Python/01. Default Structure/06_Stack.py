class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1] if not self.is_empty() else "Stack is Empty"
    
    def bottom(self):
        return self.items[0] if not self.is_empty() else "Stack is Empty"
    
    def is_empty(self):
        return self.items == []
    
    def display(self):
        print("Stack (Top->Bottom): ", *reversed(self.items))
    
    

s = Stack()
s.push(4)
s.push(6)
s.push(8)
s.push(2)

print(s.size()) # 4

print(s.top())  # 2

print(s.bottom())   # 4

s.display() # Stack (Top->Bottom):  2 8 6 4

print(s.pop()) # 2

print(s.is_empty()) # False