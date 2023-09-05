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

def goodNodes(root: TreeNode) -> int:
    def dfs(root, maxVal):
        if not root:
            return 0
        
        if root.val >= maxVal:
            res = 1
            maxVal = root.val
        else:
            res = 0
        
        res += dfs(root.left, maxVal)
        res += dfs(root.right, maxVal)
        return res
    return dfs(root, root.val)

    # goodCount = [0]
    # def dfs(root, maxVal):
    #     if not root:
    #         return
        
    #     if root.val >= maxVal:
    #         goodCount[0] += 1
    #         maxVal = root.val

    #     dfs(root.left, maxVal)
    #     dfs(root.right, maxVal)
    #     return

    # dfs(root, root.val)
    # return goodCount[0]

root = [3,1,4,3,None,1,5]
print(root)
tree = list_to_treeNode(root)
print(goodNodes(tree))