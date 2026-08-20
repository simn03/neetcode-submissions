class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        withinHoursMap = {}

        minr = math.ceil(sum(piles) / h) # O(n)
        maxr = max(piles) # O(n)

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

        # O(n)
        def isMinRate(rate: int):
            if rate > 1:
                return isWithinHours(rate) and not isWithinHours(rate - 1)

            return isWithinHours(rate)

        while minr <= maxr:
            mid = (minr + maxr) // 2

            if isMinRate(mid):
                return mid

            if isWithinHours(mid):
                maxr = mid
            else:
                minr = mid + 1

        return 0
