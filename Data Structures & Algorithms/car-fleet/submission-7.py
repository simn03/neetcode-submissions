from collections import namedtuple

Item = namedtuple('Item', ['p', 't'])

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_idx = sorted(range(len(position)), key=lambda k: -position[k])

        stack: list[Item] = []

        for i in sorted_idx:
            p = position[i]
            d = target - p
            t = d / speed[i]

            if not stack:
                stack.append(Item(p, t))
                continue

            top = stack[-1]

            if t > top.t:
                stack.append(Item(p, t))


        return len(stack)