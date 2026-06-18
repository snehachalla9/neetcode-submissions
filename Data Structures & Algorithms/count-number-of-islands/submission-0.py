from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        islands=0
        def bfs(r,c):
            q=deque([(r,c)])
            visited.add((r,c))
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1' and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands+=1
                    bfs(r,c)
        return islands
