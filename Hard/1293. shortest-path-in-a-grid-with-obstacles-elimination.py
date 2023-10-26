# 1293. Shortest Path in a Grid with Obstacles Elimination https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Runtime: 641 ms
# Memory Usage: 23.7 MB
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = collections.deque()
        visited = [[False]*n for _ in range(m)]
        q.append((0,0,k,0))
        visited = {}
        visited[(0,0,k)] = True
        dirs =[[0,1],[0,-1],[-1,0],[1,0]]
        
        while q:
            i, j, curr_k, step = q.popleft()
            if i==m-1 and j==n-1:
                return step
            if grid[i][j]==1:
                if curr_k>0:
                    curr_k -= 1
                else:
                    continue
            for d in dirs:
                x = i+d[0]
                y = j+d[1]
                if 0<=x<m and 0<=y<n and (x, y, curr_k) not in visited:
                    q.append((x,y,curr_k, step+1))
                    visited[(x,y,curr_k)] = True
        return -1