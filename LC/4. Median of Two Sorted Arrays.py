from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = set(nums1 + nums2)
        hashmap = {}
        i = 0
        for x in k:
            hashmap[i] = x
            i += 1
        if len(nums1 + nums2) == 0:
            return None
        x = len(nums1 + nums2) // 2
        if len(nums1 + nums2) % 2 == 0:
            return ((hashmap[x] + hashmap[x - 1]) / 2)
        else:
            return (hashmap[x])




s = Solution()
nums1 = []
nums2 = []
print(s.findMedianSortedArrays(nums1, nums2))
