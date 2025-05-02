#time: O(n) must traverse entire array
#space: O(1) only stores two numbers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        incumbent_min = prices[0]
        max_profit = 0
        for i, p in enumerate(prices):
            if p<incumbent_min:
                incumbent_min = p
            else:
                profit = p-incumbent_min
                if profit>max_profit:
                    max_profit = profit
            # commented part is correct but a bit slower since it always performs multiple operations
            # incumbent_min = min(incumbent_min, p)
            # max_profit = max(max_profit, p - incumbent_min)
        return max_profit
