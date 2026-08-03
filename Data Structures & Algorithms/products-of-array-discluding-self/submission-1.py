class Solution:

    # 1 2 4 6

    # 1
    # 1 1
    # 1 1 2
    # 1 1 2 8

    #.      8
    #.    8 

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        for i in range(n - 1):
            fIdx = i + 1

            res[fIdx] = res[fIdx - 1] * nums[fIdx - 1]

        postfix = nums[n - 1]

        for i in range(n - 1):
            bIdx = n - i - 2

            res[bIdx] *= postfix
            postfix *= nums[bIdx]

        return res
            
