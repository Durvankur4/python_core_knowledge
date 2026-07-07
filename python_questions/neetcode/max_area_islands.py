# # Quesiton:

 
# Medium
# Topics
# Company Tags
# Hints
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:


# # Solution:

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         island = 0
#         ROW = len(grid)
#         COL = len(grid[0])
#         max_area = 0
        
#         def dfs(r,c):
#             if r < 0 or c < 0 or r>=ROW or c>=COL or grid[r][c]!=1:
#                 return 0
#             area = 1
#             grid[r][c]= -1
#             area += dfs(r+1,c)
#             area += dfs(r-1,c)
#             area += dfs(r,c+1)
#             area += dfs(r,c-1)
#             return area

#         for i in range(ROW):
#             for j in range(COL):
#                 if grid[i][j] == 1:
#                     area_curr = dfs(i,j)
#                     max_area = max(max_area,area_curr)

#         return max_area


# # time complexity = O(n)
# # space complexity = O(n)
