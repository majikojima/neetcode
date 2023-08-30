# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_treeNode(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    queue = deque([root])
    length = len(nums)
    index = 1

    while queue:
        node = queue.popleft()
        if index < length:
            if nums[index] is not None:
                node.left = TreeNode(nums[index])
                queue.append(node.left)
            index += 1
        if index < length:
            if nums[index] is not None:
                node.right = TreeNode(nums[index])
                queue.append(node.right)
            index += 1
    return root

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

def isBalanced(root: TreeNode) -> bool:
    def dfs(root):
        if not root:
            return True, 0
        
        leftB, leftH = dfs(root.left)
        rightB, rightH = dfs(root.right)
        if abs(leftH - rightH) <= 1 and leftB and rightB:
            balance = True
        else:
            balance = False
        return balance, 1 + max(leftH, rightH)
    
    balance, _ = dfs(root)
    return balance

root = [3,9,20,None,None,15,7]
print(root)
tree = list_to_treeNode(root)
print(isBalanced(tree))