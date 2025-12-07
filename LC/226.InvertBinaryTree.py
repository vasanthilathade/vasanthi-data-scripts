from Python.Tree.BinarySearchTree.Deletion import traverse


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def Traverse(node):
    if node is None:
        return
    print(node.value, end=' ')
    Traverse(node.left)
    Traverse(node.right)


def InvertBinaryTree(tree):
    if tree is None:
        return None

    right = InvertBinaryTree(tree.right)
    left = InvertBinaryTree(tree.left)
    tree.left = right
    tree.right = left
    return tree


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print(f"Before inversion:")
    Traverse(root)
    InvertBinaryTree(tree=root)
    print(f"After inversion:")
    Traverse(root)
