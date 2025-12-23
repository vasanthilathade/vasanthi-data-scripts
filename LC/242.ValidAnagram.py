from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s)==Counter(t)
        dict1=defaultdict(int)

        dict2 = defaultdict(int)
        for char in s:
            dict1[char]+=1
        for char in t:
            dict2[char]+=1
        return dict1 == dict2

s=Solution()
print(s.isAnagram("anagram","nagaram"))