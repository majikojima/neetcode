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

def create_cycle_in_linkedlist(nums, pos):
    # First, create a linked list.
    head = list_to_linkedlist(nums)
    
    # If pos is -1, there is no cycle.
    if pos == -1:
        return head
    
    # Find the node where the cycle should start.
    cycle_start = head
    for _ in range(pos):
        cycle_start = cycle_start.next

    # Find the last node of the list.
    last_node = head
    while last_node.next:
        last_node = last_node.next

    # Create the cycle by setting the next of last_node as cycle_start.
    last_node.next = cycle_start

    return head

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

nums = [3,4,0,-4,3,4,0,-4]
pos = 1
print(nums, pos)
linked_list_with_cycle = create_cycle_in_linkedlist(nums, pos)

result = hasCycle(linked_list_with_cycle)

print(result)