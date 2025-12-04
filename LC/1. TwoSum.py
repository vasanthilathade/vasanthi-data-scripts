# https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array
from typing import List


class Brute_force_Solution:
    """
    Time complexity-O(n2)
    Space complexity- O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Brute_force_Solution()
brute_force_result = s.twoSum([2, 7, 11, 15], 9)
print(brute_force_result)


class TwoPassHashTableSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        hashmap = {}
        print(hashmap)

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        print(hashmap)
        for x in hashmap:
            print(x, hashmap[x])
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []

s = TwoPassHashTableSolution()
re = s.twoSum([2, 7, 11, 15], 9)
print(re)



class OnePassHashTableSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap :
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # If no valid pair is found, return an empty list
        return []

s = OnePassHashTableSolution()
re = s.twoSum([2, 7, 11, 15], 9)
print(re)