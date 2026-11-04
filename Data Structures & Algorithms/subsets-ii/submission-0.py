class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sol = []
        nums.sort()

        def backtrack(start):
            ans.append(sol[:])
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j-1]:
                    continue
                sol.append(nums[j])
                backtrack(j+1)
                sol.pop()
        backtrack(0)
        return ans
        