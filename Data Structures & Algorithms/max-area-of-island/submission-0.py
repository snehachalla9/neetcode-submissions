from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        def bfs(r,c):
            q=deque([(r,c)])
            visited.add((r,c))
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            area=1
            while q:
                row,col=q.popleft()
                for dr ,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if(0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited ):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        area+=1
            return area
        max_area=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    area=bfs(r,c)
                    max_area=max(max_area,area)
        return max_area
        
            
       
        