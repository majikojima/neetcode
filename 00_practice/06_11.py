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

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    groupPrev = dummy

    while True:
        kth = getKth(head, k)
        if not kth:
            break
        groupPrev.next = kth
        groupNext = kth.next

        prev = groupNext
        curr = head
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        groupPrev = head
        head = groupNext
    return dummy.next

def getKth(head, k):
    while head and k > 0:
        head = head.next
        k -= 1
    return head

head = [1,2,3,4,5]
k = 2
llh = list_to_linkedlist(head)

result = reverseKGroup(llh, k)

current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next