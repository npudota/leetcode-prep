class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        heap = []

        for n in count:
            heapq.heappush(heap, (count[n],n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for n in heap:
            res.append(n[1])
        
        return res
        
        