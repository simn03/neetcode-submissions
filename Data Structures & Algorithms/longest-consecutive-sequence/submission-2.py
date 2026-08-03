class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        groups = {}

        toVisit = set(nums)

        currMax = 0
        currStart = None

        while len(toVisit) != 0:
            curr = toVisit.pop()

            depth = 1
            start = curr

            while (curr + 1) in toVisit:
                depth += 1
                curr += 1
                toVisit.discard(curr)

            if curr + 1 == currStart:
                depth += currMax

            if depth > currMax:
                currMax = depth
                currStart = start

        return currMax