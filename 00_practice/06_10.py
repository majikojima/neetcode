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

def mergeKLists(lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    
    while len(lists) >= 2:
        mergeLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            if (i + 1) < len(lists):
                l2 = lists[i + 1]
            else:
                l2 = None
            mergeLists.append(mergeList(l1, l2))
        lists = mergeLists
    return lists[0]

def mergeList(l1: ListNode, l2: ListNode):
    dummy = ListNode()
    head = dummy
    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    if l1:
        head.next = l1
    if l2:
        head.next = l2
    return dummy.next
    

a = [1,3]
b = [1,4]
c = [2,6]
d = [3,5]
e = [1,7]
lla = list_to_linkedlist(a)
llb = list_to_linkedlist(b)
llc = list_to_linkedlist(c)
lld = list_to_linkedlist(d)
lle = list_to_linkedlist(e)
lists = [lla,llb,llc,lld,lle]

result = mergeKLists(lists)
# result = mergeList(lla,llb)

current_node = result
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next