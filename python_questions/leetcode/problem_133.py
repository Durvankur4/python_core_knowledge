# # Quesiton:

# 133. Clone Graph
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.
# # Solution:

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

#         if not node:
#             return None

#         dictt = {}
#         start = node
#         stack = [start]
#         visited = set()
#         visited.add(start)


#         while stack:
#             node = stack.pop()
#             dictt[node] = Node(val = node.val)

#             for n in node.neighbors:
#                 if n not in visited:
#                     visited.add(n)
#                     stack.append(n)

#         for o_node,n_node in dictt.items():

#             for n in o_node.neighbors:
#                 new_n = dictt[n]
#                 n_node.neighbors.append(new_n)

#         return dictt[start]

# # time complexity = O(n)
# # space complexity = O(n)
