class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def isvalidBST(self, node):
        def valid(node, left, right):
            if node is None:
                return True
            if not (node.val > left and node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(node, float("-inf"), float("inf"))


root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)

print(Solution().isvalidBST(root))
