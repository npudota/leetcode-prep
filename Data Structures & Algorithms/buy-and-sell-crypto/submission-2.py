class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = float('inf')
        maxP = 0

        for p in prices:
            min_val = min(min_val,p)
            maxP = max(p-min_val,maxP)
        
        return maxP
        