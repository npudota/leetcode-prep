class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float('inf')
        res = 0

        for i,n in enumerate(prices):
            min_val = min(n, min_val)
            res = max(res, n - min_val)
        
        return res



        