class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def successor(node):
    node = node.right
    while node is not None and node.left is not None:
        node = node.left
    return node


def traverse(node):
    if node is None:
        return
    print(node.data, end=' ')
    traverse(node.left)
    traverse(node.right)


def delNode(root, x):
    if root is None:
        return root
    if root.data > x:
        root.left = delNode(root.left, x)
    elif root.data < x:
        root.right = delNode(root.right, x)
    else:
        # handle cases
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

            # node with 2 children
        succ = successor(root)
        root.data = succ.data
        root.right = delNode(root.right, succ.data)
    return root


if __name__ == '__main__':
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    traverse(root)
    print("traversal complete")

    succ = successor(root)
    print(succ.data)
    delNode(root, 50)
    traverse(root)
