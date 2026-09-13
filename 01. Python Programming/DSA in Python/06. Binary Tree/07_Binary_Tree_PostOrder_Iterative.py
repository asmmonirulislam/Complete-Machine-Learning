from collections import deque
from typing import List

class Node:
    def __init__(self, value:int):
        self.left = None
        self.right = None
        self.data = value
        
def postOrder1(root:Node, ans=None)->List:
    if ans is None:
        ans=[]
    if not root:
        return ans
    postOrder1(root.left, ans)
    postOrder1(root.right, ans)
    ans.append(root.data)
    
    return ans

def postOrder2(root:Node)->List:
    if not root:
        return []
    left = postOrder2(root.left)
    right = postOrder2(root.right)
    return left+right+[root.data]
    

def postOrder_Iterative(root:Node)->List:
    ans = []
    if not root:
        return ans
    s = deque()
    s.append(root)
    while s:
        temp = s.pop()
        ans.append(temp.data)
        if temp.left:
            s.append(temp.left)
        if temp.right:
            s.append(temp.right)
    return list(reversed(ans))

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
print(*postOrder1(root))
print(*postOrder2(root))
print(*postOrder_Iterative(root))