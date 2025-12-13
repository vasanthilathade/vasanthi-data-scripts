from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix * res[i]
            prefix = prefix * nums[i]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * postfix
            postfix = postfix * nums[j]
        return res


print(Solution().maxProfit([1,2,3,4]))
