from typing import List
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findDuplicate(nums: List) -> int:


nums = [1,3,4,2,2]
print(findDuplicate(nums))