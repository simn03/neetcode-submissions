class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # handle array is already sorted case
        if nums[l] < nums[r]:
            return nums[l]

        if len(nums) == 1:
            return nums[0]

        while l < r:
            mid = (l + r) // 2

            ln = nums[l]
            rn = nums[r]

            if ln < nums[mid]:
                l = mid
            else:
                r = mid

        return nums[r + 1]