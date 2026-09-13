from collections import deque
from typing import List

class Node:
    def __init__(self, value:int):
        self.left = None
        self.right = None
        self.data = value
    

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

def levelOrder(root:Node)->List:
    ans = []
    if root is None:
        return ans
    q = deque()
    q.append(root)
    while q:
        level = []
        size = len(q)
        
        for i in range(size):
            temp = q.popleft()
            level.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        ans.append(level)
    return ans


root:Node = BinaryTree()
level = levelOrder(root)
for i in range(len(level)):
    for j in range(len(level[i])):
        print(level[i][j], end=' ')
    print()
    
