class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = 1

        area = 0
        n = len(height)

        while l < r < n:
            
            if height[l] <= height[r]:
                l += 1
                r = l + 1
                continue;

            localArea = 0
            
            while r < n and height[l] > height[r]:
                localArea += height[l] - height[r]
                r += 1
            
            if r < n and height[l] <= height[r]:
                area += localArea
                l = r
                r = l + 1
            else:
                l += 1
                r = l + 1

        return area