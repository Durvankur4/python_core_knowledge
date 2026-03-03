# # Quesiton:

# 547. Number of Provinces
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# # Solution:

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:

#         r = len(isConnected)
#         count = 0
#         visited = [0]*r

#         def dfs(node):
#             visited[node] = 1
#             for n in range(r):
#                 if not visited[n] and isConnected[node][n] == 1:
#                     dfs(n)

#         for i in range(r):
#             if not visited[i]:
#                 dfs(i)
#                 count += 1

#         return count
# # time complexity = O(n)
# # space complexity = O(n)
