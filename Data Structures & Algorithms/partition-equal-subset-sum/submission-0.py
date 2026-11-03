class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 == 1:
            return False

        total = total // 2

        nums = sorted(nums)

        cache = {}

        def helper(idx: int, acc: int):

            if (idx, acc) in cache:
                return cache[(idx, acc)]

            if acc == total:
                return True

            if acc > total:
                return False

            if idx == len(nums):
                return acc == total

            branch1 = helper(idx + 1, nums[idx] + acc)

            if branch1:
                return True
            
            branch2 = helper(idx + 1, acc)

            if branch2:
                return True

            cache[(idx, acc)] = False
            
            return False



        return helper(0, 0)

