class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = Node(head) if head is not None else None
        
    def insertAtBeg(self, item):
        new_data = Node(item)
        
        if self.head == None:
            self.head = new_data
        else:
            new_data.next = self.head
            self.head=new_data
            
    def insertAtMid(self, item, index):
        new_data = Node(item)
        temp = self.head
        if index == 0:
            return self.insertAtBeg(item)
        count = 0
        while temp is not None and count<index-1:
            temp = temp.next
            count+=1
        if temp is None:
            print(f"Invalid Index")
        else:
            new_data.next = temp.next
            temp.next = new_data
        
    
    def insertAtEnd(self, item):
        new_data = Node(item)
        
        if self.head != None:
            temp = self.head
            
            while temp.next != None:
                temp = temp.next
            
            temp.next = new_data
        else:
            self.head = new_data
            
    def deleteNode(self, item):
        if self.head is None:
            print(f"Linked List is Empty!")
            return
        if self.head.data == item:
            self.head = self.head.next
            return
        temp = self.head
        prev=None
        while temp is not None and temp.data != item:
            prev=temp
            temp = temp.next
        if temp is not None:
            prev.next = temp.next
        else:
            print(f"{item} is Not in the Linked List")
            
    def searchNode(self, item):
        if self.head is None:
            print(f"Linked List is Empty!")
            return
        temp = self.head
        while temp is not None:
            if temp.data == item:
                print(f"{item} found!")
                return
            temp=temp.next
        print(f"{item} is not present!")
        
    
    def display(self):
        if self.head != None:
            temp = self.head
            
            while temp != None:
                print(temp.data, end='')
                if temp.next is not None:
                    print('->', end='')
                else:
                    print('\n')
                temp=temp.next
        else:
            print(f"Linked List is Empty")
            
            
            
obj = SinglyLinkedList(20)

obj.display()   # 20

obj.insertAtEnd(30)
obj.display() # 20->30

obj.insertAtBeg(40)
obj.display()   # 40->20->30

obj.insertAtMid(15, 2)
obj.display()  # 40->20->15->30

obj.deleteNode(40)
obj.display()   # 20->15->30

obj.deleteNode(15)
obj.display()   # 20->30

obj.deleteNode(40)  # 40 is Not in the Linked List
obj.display()   # 20->30

obj.searchNode(20) # 20 found!
obj.searchNode(30)  # 30 found!
obj.searchNode(10)  # 10 is not present!