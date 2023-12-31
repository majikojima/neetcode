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

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

    
nums = [1,2,3,4,5]
n = 2
linked_list = list_to_linkedlist(nums)

result = removeNthFromEnd(linked_list, n)

current_node = result
while current_node:
    print(current_node.val)
    current_node = current_node.next
