#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findDuplicate(nums: ListNode) -> int:
    hash = set()
    curr = nums
    while curr:
        if curr.val in hash:
            return curr.val
        hash.add(curr.val)

        curr = curr.next
    return -1

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

nums = [1,3,4,2,2]
linked_nums = list_to_linkedlist(nums)
print(findDuplicate(linked_nums))