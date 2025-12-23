from typing import List


class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     print(nums, k)
    #     last_seen= {}
    #     for i, num in enumerate(nums):
    #         if num in last_seen and i-last_seen[num]<=k:
    #             return True
    #         last_seen[num]=i

    # sliding window
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = set()
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))
