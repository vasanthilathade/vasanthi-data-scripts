from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Node:
        if not preorder or not inorder:
            return None
        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


def traverse(node):
    if node is None:
        return None
    node.left = traverse(node.left)
    node.right = traverse(node.right)


root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print("hi,", root.value)
traverse(root)
