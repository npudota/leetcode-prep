class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        result = set()
        sort = sorted(nums)

        for i in range(0, len(sort) - 2, 1):
            l = i + 1
            r = len(sort) - 1
            while l < r:
                val = sort[l] + sort[r] + sort[i]
                if val == 0:
                    sol = (sort[i],sort[l], sort[r])
                    result.add(sol)
                    l += 1
                elif val < 0:
                    l += 1
                else:
                    r -= 1
        return list(result)
            
        