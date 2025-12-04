class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def orderedTraversal(node, res):
    if node is None:
        return
    # traverse throught the left side of the node
    orderedTraversal(node.left, res)
    # visit the current node
    res.append(node.data)
    # visit the right side of the node
    orderedTraversal(node.right, res)


# using the recursion
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    res = []
    orderedTraversal(root, res)

    for node in res:
        print(node, end="=")
