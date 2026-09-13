from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()
        
    def push_left(self, item):
        self.items.appendleft(item)
        
    def push_right(self, item):
        self.items.append(item)
    
    def pop_left(self):
        return self.items.popleft() if not self.is_empty() else "Deque is Empty"
        
    def pop_right(self):
        return self.items.pop() if not self.is_empty() else "Deque is Empty"
    
    def push_multiple_right(self, *args):
        self.items.extend(args)
        
    def push_multiple_left(self, *args):
        self.items.extendleft(args) # items will be added in reverse order
        
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    def left_item(self):
        return self.items[0]
    
    def right_item(self):
        return self.items[-1]
    
    def count(self, item):
        return self.items.count(item)
    
    def index(self, item):
        return self.items.index(item)
    
    def insert(self, pos, item):
        self.items.insert(pos, item)
        print(f"{item} added at location {pos}")
        self.display()
        
    def remove(self, item):
        index = self.index(item)
        self.items.remove(item)
        print(f"{item} removed from index {index}")
        self.display()
        
    def is_member(self, item):
        return item in self.items
    
    def display(self):
        if not self.is_empty():
            print("Deque (Left->right): ", *self.items)
        else:
            print("Deque is Empty")

q = Deque()

q.push_right(1) # [1]
q.push_right(2) # [1, 2]
q.push_right(3) # [1, 2, 3]
q.display() # Deque (Left->right):  1 2 3

q.push_left(4) # [4, 1, 2, 3]
q.push_left(5)  # [5, 4, 1, 2, 3]
q.push_right(6) # [5, 4, 1, 2, 3, 6]
q.display() # Deque (Left->right):  5 4 1 2 3 6

print(q.left_item()) # 5
print(q.right_item()) # 6

print(q.pop_left()) # 5
print(q.pop_right()) # 6

q.push_multiple_right(7, 1, 2)
q.display() # Deque (Left->right):  4 1 2 3 7 1 2

q.push_multiple_left(8, 9, 7)
q.display() # Deque (Left->right):  7 9 8 4 1 2 3 7 1 2

print(q.is_member(7)) # True
print(q.count(7)) # 2
print(q.index(7)) # 0
q.insert(0, 5)
# 5 added at location 0
# Deque (Left->right):  5 7 9 8 4 1 2 3 7 1 2
q.remove(7)
# 7 removed from index 1
# Deque (Left->right):  5 9 8 4 1 2 3 7 1 2