class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        nums.sort()

        def dfs(start, path, total):
            if (total == target):
                ans.append(path[:])
                return
            for j in range(start, len(nums)):
                if total + nums[j]  > target:
                    break         
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                path.pop()

        dfs(0, [], 0)
        return ans