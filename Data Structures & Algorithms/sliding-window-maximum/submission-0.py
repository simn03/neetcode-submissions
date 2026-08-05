from bisect import bisect_left, insort

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        numWindows = len(nums) - k + 1
        
        heap = sorted(nums[0:k])

        res = [0] * (numWindows)

        for i in range(numWindows):
            print(i)
            res[i] = heap[k - 1]

            left = nums[i]
            idx = bisect_left(heap, left)
            heap.pop(idx)

            if i + k < len(nums):
                right = nums[i + k]
                insort(heap, right)

        return res

