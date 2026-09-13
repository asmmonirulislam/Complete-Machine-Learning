from collections import deque
from typing import List

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def BinaryTree()->Node:
    rootNode = int(input("Enter the root node: "))
    q = deque()
    root = Node(rootNode)
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

def inOrder(root:Node)->List:
    if not root:
        return []
    left = inOrder(root.left)
    right = inOrder(root.right)
    return left+[root.data]+right

def inOrder_Iterative(root:Node)->List:
    ans = []
    s = deque() # stack
    s.append((root, False))
    while s:
        temp, flag = s.pop()
        if not flag:
            if temp.right:
                s.append((temp.right, False))
            s.append((temp, True))
            if temp.left:
                s.append((temp.left, False))
        else:
            ans.append(temp.data)
    return ans


root:Node = BinaryTree()
print(*inOrder(root))
print(*inOrder_Iterative(root))