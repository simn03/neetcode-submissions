class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        tallest = []

        maxArea = max(heights)

        for i, h in enumerate(heights):
            hIdx = i

            while tallest and tallest[-1][1] > h:
                hIdx = tallest.pop()[0]

            area = 0

            if tallest:
                for j in range(len(tallest)-1, -1, -1):
                    currHeight = tallest[j][1]
                    currWidth = i - tallest[j][0] + 1
                    currArea = currHeight * currWidth

                    if currArea <= area:
                        break
                    
                    area = currArea
            else:
                currHeight = h
                currWidth = i - hIdx + 1
                area = currHeight * currWidth

            while tallest and tallest[-1][1] == h:
                hIdx = tallest.pop()[0]

            tallest.append((hIdx, h))

            maxArea = max(maxArea, area)
            # print(tallest)

        return maxArea
                

