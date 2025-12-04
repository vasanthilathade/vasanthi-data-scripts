class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(node, res):
    if node is None:
        return
    # visit the current node
    res.append(node.data)
    print(f"currently visiting nodes: ", res)
    # left traversal
    preOrder(node.left, res)
    # right traversal
    preOrder(node.right, res)

    return (res)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

res = []
result = preOrder(root, res)
print(result)
