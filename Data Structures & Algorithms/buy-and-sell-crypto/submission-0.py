class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float('inf')
        profit = [0] * len(prices)

        for i,n in enumerate(prices):
            min_val = min(n, min_val)
            profit[i] = max(0, n - min_val)
        
        return max(profit)



        