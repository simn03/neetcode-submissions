class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        groups = {}

        currMax = 0

        roots = set(nums)

        # n
        for num in nums:
            groups[num] = num

        # n
        for num in groups.keys():
            if (num - 1) in groups:
                groups[num] = num - 1
                roots.remove(num - 1)

        for num in roots:
            depth = 1
            next = num
            while groups[next] != next:
                depth += 1
                next = groups[next]
            
            if depth > currMax:
                currMax = depth

        return currMax