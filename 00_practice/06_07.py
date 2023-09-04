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

def result(l1, l2):
    print(l1,l2)
    linked_list1 = list_to_linkedlist(l1)
    linked_list2 = list_to_linkedlist(l2)

    result = addTwoNumbers(linked_list1, linked_list2)

    current_node = result
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next
    print("")

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:


l1 = [2,4,3]
l2 = [5,6,4]
result(l1,l2)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
result(l1,l2)