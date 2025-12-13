from typing import List


class Solution:
    def maxproduct(self, nums: List[int]) ->int:
        currmax=nums[0]
        globalsum=nums[0]
        for num in nums[1:]:
            print(f"iter: {num}, currmax: {currmax}, globalsum: {globalsum}")
            currmax=max(num, currmax*num)
            globalsum=max(globalsum, currmax)
            print(f"iter: {num}, currmax: {currmax}, globalsum: {globalsum}")

        return globalsum

c=Solution()
print(c.maxproduct([-2,0,-1]))
