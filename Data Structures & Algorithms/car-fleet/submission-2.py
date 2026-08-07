from collections import namedtuple

Item = namedtuple('Item', ['p', 't'])

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        stack: list[Item] = []

        for i in range(0, n):
            p = position[i]
            d = target - p
            t = d / speed[i]

            behind: list[Item] = []

            while stack:
                top = stack[-1]

                if p < top.p and t <= top.t:
                    # print(f"Behind and faster. Joining next fleet")
                    break
                elif p < top.p and t > top.t:
                    # print(f"Behind and slower. Adding to stack.")
                    stack.append(Item(p, t))
                    break
                elif p > top.p and t >= top.t:
                    # print(f"Ahead and slower. Replacing previous fleet")
                    stack.pop()
                elif p > top.p and t < top.t:
                    # print(f"Ahead and faster. Moving ahead in stack")
                    behind.append(stack.pop())
                    break;

            if not stack:
                # print(f"No cars available. Adding new fleet")
                stack.append(Item(p, t))

            stack.extend(behind)

        return len(stack)