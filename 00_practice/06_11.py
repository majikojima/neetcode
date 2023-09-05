from typing import List

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
 
s = Solution()
head = [1,2,3,4,5]
k = 2
llh = list_to_linkedlist(head)

result = s.reverseKGroup(llh, k)

current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next