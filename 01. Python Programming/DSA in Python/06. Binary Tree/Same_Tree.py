from collections import deque

class TreeNode:
    def __init__(self, val:int, left=None, right=None)->None:
        self.val = val
        self.left = left
        self.right = right

def BinaryTree()->TreeNode:
    root = int(input())
    rootNode = TreeNode(root)
    q = deque()
    q.append(rootNode)
    
    while q:
        temp = q.popleft()
        leftChild = int(input())
        if leftChild != -1:
            temp.left = TreeNode(leftChild)
            q.append(temp.left)
        righthild = int(input())
        if righthild != -1:
            temp.right = TreeNode(righthild)
            q.append(temp.right)
        return root

def isSameTree(p:TreeNode, q:TreeNode)->bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
