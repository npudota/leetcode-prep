class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sol = []
        used = [False] * len(nums)

        def dfs():

            if len(nums) == len(sol):
                ans.append(sol[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                sol.append(nums[i])
                dfs()
                used[i] = False
                sol.pop()
        
        dfs()
        return ans
        