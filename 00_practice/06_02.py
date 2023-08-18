#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next

        if list1:
            res.next = list1
        elif list2:
            res.next = list2
        return dummy.next

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

s = Solution()

nums1 = [1,2,3,4,5]
nums2 = [1,2,3,6]
lnums1 = list_to_linkedlist(nums1)
lnums2 = list_to_linkedlist(nums2)

result = s.mergeTwoLists(lnums1, lnums2)

current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next