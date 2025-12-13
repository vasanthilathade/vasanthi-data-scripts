from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = num
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        s = {}
        for num in nums:
            s[num] = num
        if len(s) != len(nums):
            return True
        return False


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicate2(nums))
