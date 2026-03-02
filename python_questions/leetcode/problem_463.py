# # Quesiton:

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# # Solution:

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:

#         r = len(grid)
#         c = len(grid[0])
#         count = 0

#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == 1:
#                     count += 4

#                     if i > 0 and grid[i-1][j] == 1:
#                         count -= 2
#                     if j > 0 and grid[i][j-1] == 1:
#                         count -= 2
#         return count
# # time complexity = O(n)
# # space complexity = O(n)
