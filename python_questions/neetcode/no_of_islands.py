# # Quesiton:
# Number of Islands
# Medium
# Topics
# Company Tags
# Hints
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# Solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c]!='1':
                return 
            
            grid[r][c]= -1
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        count = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    
                    dfs(i,j)
                    count += 1
                    
        return count
# time complexity = O(n)
# space complexity = O(n)
