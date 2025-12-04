class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def findLowestVal(head):
    current_node= head
    lowest_val= head.data
    while current_node:
        current_val= current_node.data
        if current_val < lowest_val:
            lowest_val = current_val
        current_node=current_node.next
    return lowest_val
node1=Node(3)
node2=Node(7)
node3=Node(0)
node1.next=node2
node2.next=node3
print(findLowestVal(node1))