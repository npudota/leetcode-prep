class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        candidates.sort()

        def dfs(start, path, total):

            if target == total:
                ans.append(path[:])

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i]  > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, path, total+candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return ans
                    
        