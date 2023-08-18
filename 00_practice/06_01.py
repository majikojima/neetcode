#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

def list_to_linkedlist(nums):
    dummy = ListNode(0)
    ptr = dummy
    for n in nums:
        ptr.next = ListNode(n)
        ptr = ptr.next
    return dummy.next

s = Solution()

nums = [1,2,3,4,5]
print(nums)
linked_list = list_to_linkedlist(nums)

result = s.reverseList(linked_list)

current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next