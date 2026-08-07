class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        tallest = []

        maxArea = max(heights)

        for i, h in enumerate(heights):
            hIdx = i

            while tallest and tallest[-1][1] > h:
                hIdx = tallest.pop()[0]

            area = 0

            for j in range(len(tallest)-1, -1, -1):
                currHeight = tallest[j][1] if tallest else h
                currWidth = i - tallest[j][0] + 1 if tallest else i - hIdx + 1
                currArea = currHeight * currWidth

                if currArea <= area:
                    break
                
                area = currArea

            while tallest and tallest[-1][1] == h:
                hIdx = tallest.pop()[0]

            tallest.append((hIdx, h))

            maxArea = max(maxArea, area)
            # print(tallest)

        return maxArea
                

