import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' Heap answer 
        Time: O(nlogk)
        Space: O(n)
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
        return res '''

        #bucketsort
        bucket = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        for key,val in count.items():
            bucket[val].append(key)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for v in bucket[i]:
                if k == len(res):
                    break
                res.append(v)
        return res

            


        





       

