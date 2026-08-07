from collections import namedtuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_idx = sorted(range(len(position)), key=lambda k: -position[k])

        stack: list[int] = []

        for i in sorted_idx:
            p = position[i]
            d = target - p
            t = d / speed[i]

            if not stack:
                stack.append(t)
                continue

            top = stack[-1]

            if t > top:
                stack.append(t)


        return len(stack)