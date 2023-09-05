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

def kthSmallest(root: TreeNode, k: int) -> int:


root = [3,1,4,None,2]
k = 1
print(root, k)
tree = list_to_treeNode(root)
print(kthSmallest(tree, k))

root = [4,2,5,None,3]
k = 3
print(root, k)
tree = list_to_treeNode(root)
print(kthSmallest(tree, k))