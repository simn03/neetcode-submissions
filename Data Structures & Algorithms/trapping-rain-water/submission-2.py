class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = [0] * len(height)
        postfix = [0] * len (height)


        for i in range(len(height)):
            preIdx = i
            postIdx = len(height) - 1 - i

            if (preIdx > 0):
                prefix[preIdx] = max(height[preIdx - 1], prefix[preIdx - 1])

            if (postIdx < len(height) - 1):
                postfix[postIdx] = max(height[postIdx + 1], postfix[postIdx + 1])

        print(prefix)
        print(postfix)

        area = 0

        for i, h in enumerate(height):
            wallHeight = min(prefix[i], postfix[i])

            if wallHeight < h:
                continue

            area += wallHeight  - h

        return area