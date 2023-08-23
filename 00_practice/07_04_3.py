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
    def checkedBalance(root):
        if not root:
            return [True, 0]
        left = checkedBalance(root.left)
        right = checkedBalance(root.right)
        if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            balance = True
        else:
            balance = False
        depth = 1 + max(left[1], right[1])
        return [balance, depth]
    return checkedBalance(root)[0]

root = [4,2,7,1,3,6,9]
print(root)
tree = list_to_treeNode(root)
print(isBalanced(tree))

