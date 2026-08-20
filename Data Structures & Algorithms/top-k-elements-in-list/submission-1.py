class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for c in count.keys():
            bucket[count[c]].append(c)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if(len(res) == k):
                    return res



        
        


        
        

        