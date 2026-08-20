class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # handle array is already sorted case
        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2

            ln = nums[l]
            rn = nums[r]

            if rn < nums[mid]:
                l = mid + 1
            else:
                r = mid

        return nums[l]