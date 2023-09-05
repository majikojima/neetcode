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

def isValidBST(root: TreeNode) -> bool:


root = [2,1,3]
print(root)
tree = list_to_treeNode(root)
print(isValidBST(tree))

root = [5,1,4,None,None,3,6]
print(root)
tree = list_to_treeNode(root)
print(isValidBST(tree))

root = [5,4,6,None,None,3,7]
print(root)
tree = list_to_treeNode(root)
print(isValidBST(tree))
