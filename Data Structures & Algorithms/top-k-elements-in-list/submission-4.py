import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        
        for n in nums:
            count[n] = count.get(n,0) + 1
        
        heap = []
        for key,val in count.items():
            heapq.heappush(heap, (val,key))
            if (len(heap) > k):
                heapq.heappop(heap)
        
        res = []
        for n in heap:
            res.append(n[1])
        
        return res



       

