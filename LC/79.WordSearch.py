from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        length = len(word)
        path = set()

        def dfs(r, c, curr):
            if curr == length:
                return True
            if (r < 0 or c < 0 or
                    r >= ROWS or c >= COLS or
                    board[r][c] != word[curr] or
                    (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, curr + 1) or
                   dfs(r - 1, c, curr + 1) or
                   dfs(r, c + 1, curr + 1) or
                   dfs(r, c - 1, curr + 1)
                   )
            path.remove((r, c))
            return res

        for x in range(ROWS):
            for y in range(COLS):
                result = dfs(x, y, 0)
                if result:
                    return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
s = Solution()
print(s.exist(board, "ABCCED"))
print(s.exist(board, "ABCCEp"))
