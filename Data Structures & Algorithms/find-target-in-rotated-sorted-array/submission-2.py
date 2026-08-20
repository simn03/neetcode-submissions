class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2


            if nums[l] <= nums[m] and nums[l] <= target <= nums[m]:
                r = m
            elif nums[l] <= nums[m]:
                l = m + 1
            elif nums[l] <= target or nums[m] >= target:
                r = m
            else:
                l = m

        return l if nums[l] == target else -1

