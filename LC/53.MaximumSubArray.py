from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) ->int:
        currmax=nums[0]
        globalsum=nums[0]
        for num in nums[1:]:
            print(f"iter: {num}, currmax: {currmax}, globalsum: {globalsum}")
            currmax=max(num, currmax+num)
            globalsum=max(globalsum, currmax)
            print(f"iter: {num}, currmax: {currmax}, globalsum: {globalsum}")

        return globalsum

c=Solution()
print(c.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
