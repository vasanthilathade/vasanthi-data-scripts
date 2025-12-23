from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        d = defaultdict(int)
        maxFreq, maxCount = 0, 0
        for R in range(len(s)):
            d[s[R]] += 1
            if d[s[R]] > maxFreq:
                maxFreq = d[s[R]]
            while R - L + 1 -maxFreq> k:
                d[s[L]] -= 1
                L += 1
            maxCount = max(maxCount, R - L + 1)
        return maxCount


s = Solution()
print( s.characterReplacement("ABAB", 2))
