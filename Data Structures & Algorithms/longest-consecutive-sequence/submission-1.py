class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        groups = {}

        currMax = 0

        numSet = set(nums)
        roots = set(nums)

        # n
        for num in numSet:
            if (num - 1) in roots:
                groups[num] = num - 1
                roots.remove(num - 1)

        for num in roots:
            depth = 1
            next = num
            while next in groups:
                depth += 1
                next = groups[next]
            
            if depth > currMax:
                currMax = depth

        return currMax