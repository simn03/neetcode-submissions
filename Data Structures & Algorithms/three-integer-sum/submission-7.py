class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)

        triplesSet = set()

        prev = None

        for i, num in enumerate(nums):
            if num == prev:
                continue;
            
            target = 0 - num

            l = i + 1
            r = len(nums) - 1

            while l < r:
                tmp = nums[l] + nums[r]

                if (nums[l] > target):
                    break

                if tmp == target:
                    triplesSet.add((num, nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif tmp < target:
                    l += 1
                elif tmp > target:
                    r -= 1
            
            prev = num

        triples = list(map(lambda x: [x[0], x[1], x[2]], triplesSet))

        return triples
