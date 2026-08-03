class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            map[n] = i

        for i, n in enumerate(nums):
            key = target - n;
            
            if (key in map and map[key] != i):
                return sorted([map[key], i])
