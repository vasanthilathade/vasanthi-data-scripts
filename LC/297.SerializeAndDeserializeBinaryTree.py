class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Codec:
    def serialize(self, node):

        s = []

        def dfs(node):
            if node is None:
                s.append("N")
                return
            s.append(str(node.value))
            dfs(node.left)
            dfs(node.right)

        dfs(node)
        return ",".join(s)

    def deserialize(self, s):
        vals = s.split(",")
        self.i = 0

        def dfs():
            print("i is: ", self.i)
            if vals[self.i] == "N":
                self.i += 1
                return None
            root = Node(int(vals[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


def main():
    codec = Codec()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    serialized = codec.serialize(root)
    print(serialized)
    deserialized = codec.deserialize(serialized)
    print("Deserialized root value:", deserialized.value)  # just to check
    print("Left child:", deserialized.left.value)
    print("Right child:", deserialized.right.value)


main()
