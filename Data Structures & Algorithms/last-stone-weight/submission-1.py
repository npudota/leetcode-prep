class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while 1 < len(max_heap):
            stoneX = -heapq.heappop(max_heap)
            stoneY = -heapq.heappop(max_heap)

            if stoneX == stoneY:
                continue
            elif stoneY < stoneX:
                heapq.heappush(max_heap, (stoneX-stoneY) * -1)
        
        return 0 if len(max_heap) == 0 else -max_heap[0]



        