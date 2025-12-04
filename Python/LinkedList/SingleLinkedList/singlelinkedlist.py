class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def traverseAndPrint(head):
    current_node=head
    while current_node:
        print(f'current node -> {current_node.data}, end is ->')
        current_node=current_node.next
    print("null")

node1=Node(3)
node2=Node(4)
node3=Node(6)
node1.next=node2
node2.next=node3

traverseAndPrint(node1)