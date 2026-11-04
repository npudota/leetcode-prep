class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        sol = []

        def backtrack(start):
            if (sum(sol) == target):
                ans.append(sol[:])
                return
            elif (sum(sol) > target):
                return
            for j in range(start, len(nums)):         
                sol.append(nums[j])
                backtrack(j)
                sol.pop()
        backtrack(0)
        return ans