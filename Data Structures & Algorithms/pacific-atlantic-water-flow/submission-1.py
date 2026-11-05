class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pac = [[False for _ in range(cols)] for _ in range(rows)]
        atl = [[False for _ in range(cols)] for _ in range(rows)]


        ans = []

        def dfs(r,c,val, visited):
            if r >= rows or c >= cols or  r < 0 or c < 0 or visited[r][c] == True or heights[r][c] < val:
                return
            if heights[r][c] >= val:
                visited[r][c] = True
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
        
        for r in range(rows):
            dfs(r, 0, -1,pac)
            dfs(r, cols-1, -1,atl)
        
        for c in range(cols):
            dfs(0, c, -1,pac)
            dfs(rows-1, c, -1,atl)

        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    ans.append([r,c])
        
        return ans
        
        
            
            
                

            
        