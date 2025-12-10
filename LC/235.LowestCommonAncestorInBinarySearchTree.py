from pygments.lexers import q


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        while curr:
            if p.data < curr.data and q.data < curr.data:
                curr = curr.left
            elif p.data > curr.data and q.data > curr.data:
                curr = curr.right
            else:
                return curr


root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)

p = Node(0)
q = Node(5)
res = Solution().lowestCommonAncestor(root, p, q)
print(res.data)
