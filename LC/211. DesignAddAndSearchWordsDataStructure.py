class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class wordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word)->None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_word = True

    def search(self, word)->bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_word

        return (dfs(0, self.root))


k = wordDictionary()
k.addWord("hello")
print(k.search("h..o"))
