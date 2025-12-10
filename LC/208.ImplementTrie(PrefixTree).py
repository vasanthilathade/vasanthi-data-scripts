class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def traverse(self):
        result = []
        self._dfs(self.root, "", result)
        return result

    def _dfs(self, node, path, result):
        if node.isEnd:
            result.append(path)

        for ch, child in node.children.items():
            self._dfs(child, path + ch, result)

    def insert(self, word):
        curr = self.root
        for i in word:

            if i not in curr.children:
                curr.children[i] = TrieNode()

            curr = curr.children[i]
        curr.isEnd = True

    def search(self, word) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.isEnd

    def startsWith(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True


k = Solution()
k.insert("apple")
print(k.traverse())
print(k.search("apple"))
print(k.startsWith("app"))
