from collections import namedtuple

Item = namedtuple('Item', ['p', 't'])

def formatItem(item: Item):
    return Item(item.p, round(item.t, 3))

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

                # print(f"Item(p={p}, t={t})   =>   {formatItem(top)}")

                if p < top.p and t <= top.t:
                    # print(f"  Behind and faster. Joining next fleet")
                    break
                elif p < top.p and t > top.t:
                    # print(f"  Behind and slower. Adding new fleet.")
                    stack.append(Item(p, t))
                    break
                elif p > top.p and t >= top.t:
                    # print(f"  Ahead and slower. Replacing previous fleet")
                    stack.pop()
                elif p > top.p and t < top.t:
                    # print(f"  Ahead and faster. Moving in front of next fleet")
                    behind.append(stack.pop())
                

            if not stack:
                # print(f"No cars available. Adding new fleet")
                stack.append(Item(p, t))

            while behind:
                stack.append(behind.pop())

            # print(list(map(formatItem, stack)))

        return len(stack)