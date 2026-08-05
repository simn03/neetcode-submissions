class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()

        def insert(i):
            num = nums[i]
            while q and q[-1][0] < i and q[-1][1] < num:
                q.pop()

            q.append((i, num))

        def remove(i):
            while q and q[0][0] < i:
                q.popleft()

        for i in range(k):
            insert(i)

        num_windows = len(nums) - k + 1

        res = [0] * num_windows

        for i in range(num_windows):
            
            remove(i)
            res[i] = q[0][1]
            
            end = i + k

            if end < len(nums):
                insert(end)

            

        return res
