# https://leetcode.com/problems/subtree-of-another-tree/

# This can be achieved using the serialization

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isSubTree(subtree, root):
    def serialize(node):
        if node is None:
            return "@"
        return "~" + str(node.value) + "#" + serialize(node.left) + serialize(node.right)

    return serialize(subtree) in serialize(root)


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(2)

    # sub tree
    subtree = Node(4)
    subtree.left = Node(1)
    subtree.right = Node(2)

    print(isSubTree(subtree, root))


# time complexity =O(MN)
# space complexity = O(M+N)
