# Definition for a binary tree node.
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeNode_to_list(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            if node.left or node.right or queue:  # Keep appending for remaining levels
                queue.append(node.left)
                queue.append(node.right)
        else:
            result.append(None)  # Keep appending None for missing nodes in this level
    while result[-1] is None:  # Remove trailing None values
        result.pop()
    return result

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
result = buildTree(preorder, inorder)
print(treeNode_to_list(result))