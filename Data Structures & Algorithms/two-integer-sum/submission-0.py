class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)

        i = 0
        j = len(nums) - 1


        while i != j:
            a = nums[i]
            b = nums[j]

            abSum = a + b

            if (abSum == target):
                return [i, j]

            if (abSum < target):
                i += 1

            if (abSum > target):
                j -= 1

        return [0, 0]