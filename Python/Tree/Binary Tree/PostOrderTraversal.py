class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrder(node, res):
    if node is None:
        return
    postOrder(node.left, res)
    postOrder(node.right, res)
    res.append(node.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

res = []
postOrder(root, res)
for node in res:
    print(node, end=' ')
