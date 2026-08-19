class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (j + i) // 2

            if i == j:
                return i if nums[i] == target else -1

            if nums[i] <= target <= nums[mid]:
                j = mid
            elif nums[mid + 1] <= target <= nums[j]:
                i = mid + 1
            else: 
                return -1

        return -1