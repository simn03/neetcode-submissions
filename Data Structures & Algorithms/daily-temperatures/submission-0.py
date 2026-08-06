class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            val = temperatures[i]
            
            while(max_stack and max_stack[-1][0] <= val):
                max_stack.pop()

            if max_stack:
                res[i] = max_stack[-1][1] - i
            else: 
                res[i] = 0

            max_stack.append((val, i))
        
        return res