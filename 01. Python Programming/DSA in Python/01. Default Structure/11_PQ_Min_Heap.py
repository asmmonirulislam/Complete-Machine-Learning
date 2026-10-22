import heapq

# min_heap

class PriorityQueue:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
    
    def heappush(self, item):
        heapq.heappush(self.heap, item)
        print(f"{item} inserted to Heap")
    
    def heappop(self):
        if self.heap:
            element =  heapq.heappop(self.heap)
            print(f"{element} popped!")
        else:
            print(f"Heap is Empty, can not Pop!")
    
    # Push item on the heap, then pop and return the smallest item from the heap
    def heappushpop(self, item):
        element = heapq.heappushpop(self.heap, item)
        print(f"{element} popped!")
        
    
    # Pop and return the smallest item from the heap, and also push the new item.
    def heapreplace(self, item):
        if self.heap:
            element = heapq.heapreplace(self.heap, item)
            print(f"{element} popped!")
        else:
            print(f"The Heap is Empty!")
    
    def display(self):
        element = [heapq.heappop(self.heap) for i in range(len(self.heap))]
        print(*element)

obj = PriorityQueue()
# heap = [-4, 9, 1, 6, 3, 4, -9, -8]
obj.heappush(-4)        
obj.heappush(9)        
obj.heappush(1)        
obj.heappush(6)        
obj.heappush(3)        
obj.heappush(4)        
obj.heappush(-9)        
obj.heappush(-8)
obj.heappop()  # -9 popped!
  
obj.heappushpop(-5)  # -8 popped!
obj.heapreplace(-6)  # -5 popped!     