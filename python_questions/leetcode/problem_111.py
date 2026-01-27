# # Quesiton:
# 111. Minimum Depth of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         que = []
#         depth = 1
#         que.append((root,depth))

#         while que:
#             curr,d = que.pop(0)

#             if curr.left is None and curr.right is None:
#                 return d

#             if curr.left:
#                 que.append((curr.left,d+1))
#             if curr.right:
#                 que.append((curr.right,d+1))
#         return depth
# # time complexity = O(n)
# # space complexity = O(n)
