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

def reorderList(head: ListNode) -> None:


head = [1,2,3,4]
print(head)
head = list_to_linkedlist(head)
reorderList(head)
current_node = head
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next

head = [1,2,3,4,5]
print(head)
head = list_to_linkedlist(head)
reorderList(head)
current_node = head
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next