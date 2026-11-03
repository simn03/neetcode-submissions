class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def helper(remaining: int) -> int | None:

            if remaining in cache:
                return cache[remaining]

            if remaining == 0:
                return 0

            minCoins = None

            for coin in coins:
                if coin > remaining:
                    continue
                
                numCoins = helper(remaining - coin)
                
                if numCoins is None:
                    continue
                
                minCoins = min(numCoins + 1, minCoins) if minCoins is not None else numCoins + 1

            cache[remaining] = minCoins

            return minCoins

        res = helper(amount)

        if res is None:
            return -1

        return res

            
