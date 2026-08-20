class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(n log n)
        piles = sorted(piles, reverse=True)

        minr = math.ceil(len(piles) / h) # O(1)
        maxr = piles[0] # O(1)

        rate = minr

        # O(n)
        def isWithinHours(rate: int):
            total = 0

            for pile in piles:
                total += math.ceil(pile / rate)
                if total > h:
                    return False

            return True

        while not isWithinHours(rate) and rate < maxr:
            rate += 1

        return rate
