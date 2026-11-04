class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        sol = []
        candidates.sort()

        def dfs(start, total):

            if total == target:
                res.append(sol[:])
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] + total > target:
                    break
                sol.append(candidates[i])
                dfs(i+1, candidates[i] + total)
                sol.pop()
        
        dfs(0,0)
        return res

        