from collections import namedtuple

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack: list[float] = []

        for p, s in sorted(zip(position, speed), reverse=True):
            d = target - p
            t = d / s

            if not stack:
                stack.append(t)
                continue

            top = stack[-1]

            if t > top:
                stack.append(t)


        return len(stack)