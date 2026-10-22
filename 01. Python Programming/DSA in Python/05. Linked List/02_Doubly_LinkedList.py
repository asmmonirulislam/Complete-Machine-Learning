class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertNode(self, item, index=None):
        newNode = Node(item)
        
        
        # Case 1: if the index is negative
        if index is not None and index <= 0:
            print(f"Invalid Index ({index})")
            return
        
        # Case 2: if there is no index input (item will be inserted at the end)
        if index is None:
            if self.head is None:
                self.head = newNode
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            return
        
        index-=1
        
        # Case 3: if the index is 0 (item will be inserted at the beginning)
        if index == 0:
            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode
            return
        
        temp = self.head
        count = 0
        
        while temp and count<index-1:
            temp = temp.next
            count+=1
        
        if not temp:
            print(f"Invalid index {index}")
            return
        
        nextNode = temp.next
        
        newNode.next = nextNode
        newNode.prev = temp
        temp.next = newNode
        
        if nextNode:
            nextNode.prev = newNode
                
    def deleteNode(self, item):
        if not self.head:
            print(f"Linked List is Empty, can not delete any item")
            return
        
        if self.head.data == item:
            self.head=self.head.next
            self.head.prev = None
            return
        
        temp = self.head
        while temp and temp.data!=item:
            temp=temp.next
        if not temp:
            print(f"{item} not found in the linked list")
            return
        prevNode = temp.prev
        nextNode = temp.next
        prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='')
            if not temp.next is None:
                print('<->', end='')
            else:
                print('\n')
            temp=temp.next    
            
    def display_backward(self):
        if not self.head:
            print(f"Linked List is empty!")
            return
        
        temp = self.head
        
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end='')
            if temp.prev:
                print('<->', end='')
            else:
                print('\n', end='')
            temp=temp.prev
            
            
obj = DoublyLinkedList()
obj.insertNode(30)
obj.insertNode(20)
obj.insertNode(10)
obj.display()   # 30<->20<->10

obj.insertNode(5, 1)
obj.display()   # 5<->30<->20<->10

obj.insertNode(15, 3)
obj.display()   # 5<->30<->15<->20<->10

obj.insertNode(25, 5)
obj.display()   # 5<->30<->15<->20<->25<->10

obj.insertNode(27, 8)   # Invalid index 7
obj.display()   # 5<->30<->15<->20<->25<->10

obj.deleteNode(5)
obj.display()   # 30<->15<->20<->25<->10

obj.deleteNode(25)
obj.display()   # 30<->15<->20<->10

obj.deleteNode(10)
obj.display()   # 30<->15<->20

obj.display_backward()  # 20<->15<->30