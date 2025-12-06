class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(root):
    if root is None:
        return 0
    lheight = maxDepth(root.left)
    rheight = maxDepth(root.right)
    return max(lheight, rheight) + 1


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    x = maxDepth(root)
    print(f"height is: {x}")
