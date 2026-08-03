class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        forward = [1] * n
        backward = [1] * n

        forward[0] = nums[0]
        backward[n-1] = nums[n-1]

        for i in range(n - 1):
            fIdx = i + 1;
            bIdx = n - (i + 2)

            forward[fIdx] = forward[fIdx - 1] * nums[fIdx]
            backward[bIdx] = backward[bIdx + 1] * nums[bIdx]

        res = [0] * n;

        for i in range(n):
            val = 1;

            if i > 0:
                val *= forward[i-1]
            if i < n - 1:
                val *= backward[i+1]

            res[i] = val

        return res
