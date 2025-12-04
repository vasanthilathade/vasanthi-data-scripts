class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseAndPrint(head):
    current_node = head
    while current_node:
        print(f'current node -> {current_node.data}, end is ->')
        current_node = current_node.next
    print("null")


def deleteNode(head, node_to_delete):
    if head == node_to_delete:
        print("hi")
        return head.next
    current_node = head
    while current_node.next and current_node.next != node_to_delete:
        current_node = current_node.next
    if current_node.next is None:
            return head
    current_node.next=current_node.next.next
    return head

node1 = Node(3)
node2 = Node(4)
node3 = Node(6)
node4 = Node(10)
node1.next = node2
node2.next = node3
node3.next=node4

traverseAndPrint(node1)
s=deleteNode(node1, node1)
traverseAndPrint(s)
