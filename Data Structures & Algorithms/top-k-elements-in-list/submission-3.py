class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for _ in range(len(nums) + 1)]
        count = defaultdict(int)
        res = []
        
        for n in nums:
            count[n] += 1
        
        for n in count:
            bucket[count[n]].append(n)
        
        for l in reversed(bucket):
            for n in l:
                if (k == 0):
                    return res
                res.append(n)
                k -= 1
        
        return res

