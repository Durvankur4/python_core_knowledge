# # Quesiton:
# 200. Number of Islands
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# # Solution:
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

#         r = len(grid)
#         c = len(grid[0])

#         islands_no = 0

#         def dfs(i,j):

#             if i < 0 or j < 0 or i >= r or j >= c or grid[i][j]!="1":
#                 return
#             else:
#                 grid[i][j] = 0
#                 dfs(i+1,j)
#                 dfs(i,j+1)
#                 dfs(i-1,j)
#                 dfs(i,j-1)

#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == "1":
#                     islands_no += 1
#                     dfs(i,j)
#         return islands_no

# # time complexity = O(n)
# # space complexity = O(n)
