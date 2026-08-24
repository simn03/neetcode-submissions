class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slower = 0

        while slower != slow:
            slower = nums[slower]
            slow = nums[slow]

        return slow