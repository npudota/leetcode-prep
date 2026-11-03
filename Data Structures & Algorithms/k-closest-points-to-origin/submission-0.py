class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        res = []

        for pt in points:
            x, y = pt
            distance = math.sqrt((x - 0)**2 + (y - 0)**2) * -1
            heapq.heappush(minHeap, (distance,pt))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        for distance, pt in minHeap:
            res.append(pt)
        return res

            
        




        