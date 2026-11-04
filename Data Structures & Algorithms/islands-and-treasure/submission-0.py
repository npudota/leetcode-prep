class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        dist = 0
        while q:
            size = len(q)
            dist += 1
            for i in range(size):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0 or grid[nr][nc] == -1:
                        continue
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist
                        q.append((nr,nc))

        