class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)

        triples = []

        prev = None

        for i, num in enumerate(nums):
            if num == prev:
                continue;
            
            target = 0 - num

            l = i + 1
            r = len(nums) - 1

            while l < r:
                tmp = nums[l] + nums[r]

                if tmp == target:
                    triples.append([num, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    continue;
                elif tmp < target:
                    l += 1
                elif tmp > target:
                    r -= 1
            
            prev = num

        return triples
