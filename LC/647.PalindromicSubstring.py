class Solution:
    def countSubstrings(self, s: str) -> list:
        n = len(s)
        ans =[]
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(n):
            dp[i][i] = True
            ans.append(s[i])
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans.append(s[i:i+2])

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans.append(s[i:j+1])


        return ans


s = Solution()
print(s.countSubstrings("aaa"))