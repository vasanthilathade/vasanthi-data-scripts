class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maxpathsum(root):
    res = [root.value]

    def dfs(node):
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        left = max(0, left)
        right = max(0, right)

        # split result
        res[0] = max(res[0], node.value + left + right)
        return max(node.value + left, root.value + right)

    dfs(root)
    return res[0]


def main():
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(maxpathsum(root))


main()
