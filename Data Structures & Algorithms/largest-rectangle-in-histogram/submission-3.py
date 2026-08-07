class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        tallest = []

        maxArea = max(heights)

        for i, h in enumerate(heights):
            hIdx = i

            while tallest and tallest[-1][1] >= h:
                hIdx = tallest.pop()[0]

            currHeight = tallest[-1][1] if tallest else h
            currWidth = i - tallest[-1][0] + 1 if tallest else i - hIdx + 1
            currArea = currHeight * currWidth
            # print(f"{currHeight} * {currWidth} = {currArea}")

            tallest.append((hIdx, h))

            maxArea = max(maxArea, currArea)
            # print(tallest)

        return maxArea
                

