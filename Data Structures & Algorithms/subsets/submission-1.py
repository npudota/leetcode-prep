class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sol = []

        def dfs(start):

            ans.append(sol[:])

            for i in range(start, len(nums)):

                sol.append(nums[i])
                dfs(i + 1)
                sol.pop()
        
        dfs(0)
        return ans
        