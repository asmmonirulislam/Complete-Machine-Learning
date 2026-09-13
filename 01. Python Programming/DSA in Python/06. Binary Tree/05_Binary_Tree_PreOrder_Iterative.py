from collections import deque
from typing import List

class Node:
    def __init__(self, value:int):
        self.left = None
        self.right = None
        self.data = value
        
def preOrder(temp:Node)->int:
    if temp is None:
        return
    print(temp.data, end=" ")
    preOrder(temp.left)
    preOrder(temp.right)
    
def preOrder_Iterative(root : Node)->List:
    ans = []
    if not root:
        return ans
    s = deque()
    s.append(root)
    while s:
        temp = s.pop()
        ans.append(temp.data)
        if temp.right:
            s.append(temp.right)
        if temp.left:
            s.append(temp.left)
    return ans 

def BinaryTree()->Node:
    rootNode = int(input("Enter the root node: "))
    root = Node(rootNode)
    
    q = deque()
    q.append(root)
    
    while q:
        temp = q.popleft()
        leftChild = int(input(f"Enter the left child of {temp.data}: "))
        if leftChild != -1:
            temp.left = Node(leftChild)
            q.append(temp.left)
        rightChild = int(input(f"Enter the right child of {temp.data}: "))
        if rightChild != -1:
            temp.right = Node(rightChild)
            q.append(temp.right)
    
    return root


root:Node = BinaryTree()
preOrder(root)
print()
it = preOrder_Iterative(root)
print(*it)