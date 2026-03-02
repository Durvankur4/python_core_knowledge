# # Quesiton:
# 695. Max Area of Island
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# # Solution:

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

#         r ,c = len(grid),len(grid[0])
#         islands = 0
#         max_islands = []

#         def dfs(i,j):
#             count = 0
#             if i < 0 or j < 0 or i >= r or j >= c or grid[i][j]!=1:
#                 return 0
#             else:
#                 count += 1
#                 grid[i][j] =0
#                 count += dfs(i+1,j)
#                 count += dfs(i-1,j)
#                 count += dfs(i,j+1)
#                 count += dfs(i,j-1)
#             return count


#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == 1:
#                     islands += 1
#                     max_islands.append(dfs(i,j))

#         return max(max_islands) if max_islands else 0

# # time complexity = O(n)
# # space complexity = O(n)
