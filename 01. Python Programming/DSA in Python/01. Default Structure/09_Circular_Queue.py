class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1
    
    def isFull(self):
        return (self.rear + 1)% self.size == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def enqueue(self, item):
        if self.isFull():
            print(f"Queue is Full, can not insert {item}")
        elif self.isEmpty():
            self.front = self.rear = 0
            self.items[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item
    
    def dequeue(self):
        if self.isEmpty():
            print(f"Queue is Empty, can not dequeue")
        elif self.front == self.rear:
            self.items[self.front]=None
            self.front = self.rear = -1
        else:
            self.items[self.front]=None
            self.front = (self.front+1)%self.size
            
    def display(self):
        if self.isEmpty():
            print("Queue is Empty") 
        else:
            elements = []
            
            i = self.front
            
            while True:
                elements.append(self.items[i])
                if i==self.rear:
                    break
                i = (i+1)%self.size
            print("Elements of the Circular Queue: ", *elements)
        
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6) # Queue is Full, can not insert 6
cq.display() # Elements of the Circular Queue:  1 2 3 4 5
cq.dequeue() 
cq.enqueue(6)
cq.display() # Elements of the Circular Queue:  2 3 4 5 6