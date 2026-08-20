class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        withinHoursMap = {}

        # O(n log n)
        piles = sorted(piles, reverse=True)

        minr = math.ceil(sum(piles) / h) # O(n)
        maxr = piles[0] # O(1)

        rate = minr

        # O(n)
        def isWithinHours(rate: int):
            if rate in withinHoursMap:
                return withinHoursMap[rate]

            total = 0

            res = True

            for pile in piles:
                total += math.ceil(pile / rate)
                if total > h:
                    res = False
                    break;

            withinHoursMap[rate] = res

            return res

        def isMinRate(rate: int):
            if rate > 0:
                return isWithinHours(rate) and not isWithinHours(rate - 1)

            return isWithinHours(rate)

        prev = rate
        growth = 1
        
        while True:
            if isMinRate(rate):
                return rate
            
            if not isWithinHours(rate):
                prev = rate
                rate += growth
                growth *= 2
            else:
                rate = prev
                growth = 1

        return rate
