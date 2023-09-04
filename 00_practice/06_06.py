# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def createRandomList(data: list) -> Node:
    if not data:
        return None
    
    # make nodelist
    nodes = [Node(x[0]) for x in data]

    # setting
    for i, item in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if item[1]:
            nodes[i].random = nodes[item[1]]

    return nodes[0]

def copyRandomList(head: Node) -> Node:


head_data = [[10,None],[11,0],[12,4],[13,2],[14,0]]
head = createRandomList(head_data)
result = copyRandomList(head)
while head:
    print(f"head.val, head.random: {head.val}, {head.random}")
    head = head.next
while result:
    print(f"result.val, result.random: {result.val}, {result.random}")
    result = result.next