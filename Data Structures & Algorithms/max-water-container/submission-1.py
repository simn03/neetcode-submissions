class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxVolume = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            volume = width * height

            maxVolume = max(volume, maxVolume)

            if (heights[l] < heights[r]):
                while l < r and heights[l] < heights[r]:
                    l += 1
            else:
                while l < r and heights[l] >= heights[r]:
                    r -= 1

        return maxVolume