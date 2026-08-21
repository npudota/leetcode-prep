class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for n in numsSet:
            if(n-1 not in numsSet):
                i = n
                count = 1
                while(i + 1 in numsSet):
                    count += 1
                    i += 1
                res = max(count,res)
        return res
                    
                
        