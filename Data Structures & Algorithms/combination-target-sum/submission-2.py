class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        sol = []
        nums.sort()

        def dfs(start, total):

            if total == target:
                res.append(sol[:])
            
            for i in range(start, len(nums)):

                if nums[i] + total > target:
                    break
                sol.append(nums[i])
                dfs(i, nums[i] + total)
                sol.pop()
        
        dfs(0,0)
        return res


        