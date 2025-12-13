from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWCOUNT, COLCOUNT = len(board), len(board[0])
        trie = {}
        matched_words = []
        word_mark = '$'
        for word in words:
            current_node = trie
            for letter in word:
                current_node = current_node.setdefault(letter, {})
            current_node[word_mark] = word

        def backtracking(row, col, parent):
            letter = board[row][col]
            current_node = parent[letter]

            matched = current_node.pop(word_mark, False)

            if matched:
                matched_words.append(matched)
            board[row][col] = "#"
            for rowoffset, columnoffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newrow = row + rowoffset
                newcol = col + columnoffset

                if (newrow < 0 or newcol < 0 or newrow >= ROWCOUNT or newcol >= COLCOUNT):
                    continue

                if not board[newrow][newcol] in current_node:
                    continue

                backtracking(newrow, newcol, current_node)
            board[row][col] = letter
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not current_node:
                parent.pop(letter)

        for row in range(ROWCOUNT):
            for col in range(COLCOUNT):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched_words


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
print(Solution().findWords(board, words))
