class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sol = []

        def backtrack(i):
            ans.append(sol[:])
            for j in range(i, len(nums)):
                sol.append(nums[j])
                backtrack(j+1)
                sol.pop()
        
        backtrack(0)
        return ans
        