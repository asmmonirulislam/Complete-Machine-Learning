class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head) if head is not None else None
    
    def insertAtBegining(self, item:int)->None:
        item = Node(item)
        if self.head is None:
            self.head = item
        else:
            item.next = self.head
            self.head = item
            
    def insertAtMid(self, item:int, loc:int)->None:
        item = Node(item)
        count=0
        temp = self.head
        while temp and count<(loc-1):
            temp = temp.next
            count+=1
        if temp is None:
            print('Invalid Index')
        else:
            item.next = temp.next
            temp.next = item
            
    def deleteItem(self, item:int)->None:
        temp = self.head
        prev = None
        while temp and temp.val != item:
            prev=temp
            temp = temp.val
        if temp is None:
            print('Item not found')
        else:
                        