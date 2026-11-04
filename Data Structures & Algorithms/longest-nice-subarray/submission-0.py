class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        used = 0
        l = 0
        longest = 0

        for r, num in enumerate(nums):
            while used & num:
                used ^= nums[l]
                l += 1
            used |= num
            longest = max(longest, r - l + 1)

        return longest