class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def front(self):
        return self.items[0] if not self.is_empty() else "Stack is Empty"
    
    def back(self):
        return self.items[-1] if not self.is_empty() else "Stack is Empty"
    
    def display(self):
        if not self.is_empty(): print("Queue (Front->Back): ", *self.items)
        else: print("Stack is Empty")

    
q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

print(q.size()) # 5
print(q.front()) # 1
print(q.back()) # 5
print(q.is_empty()) # False
q.display() # Queue (Front->Back):  1 2 3 4 5
print(q.pop())  # 1