class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        sortedIdxs = sorted(range(len(nums)), key=lambda i: nums[i])

        i = 0
        j = len(nums) - 1

        while i != j:
            abSum = sortedNums[i] + sortedNums[j]             

            if (abSum < target):
                i += 1
            elif (abSum > target):
                j -= 1
            else:
                break;

        return [sortedIdxs[i], sortedIdxs[j]]