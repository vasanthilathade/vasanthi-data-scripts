# https://leetcode.com/problems/same-tree/description/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data == root2.data and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)


if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    # second tree
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    print(sameTree(root1, root2))
