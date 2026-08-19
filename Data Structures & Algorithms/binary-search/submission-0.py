class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i != j - 1:
            mid = (j + i) // 2

            if nums[i] < target < nums[mid]:
                j = mid
            elif nums[mid] < target < nums[j]:
                i = mid
            elif target == nums[mid]:
                return mid
            elif target == nums[i]:
                return i
            elif target == nums[j]:
                return j
            else:
                return -1

        return -1