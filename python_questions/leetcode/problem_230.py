# # Quesiton:

# 230. Kth Smallest Element in a BST
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         count = 0
#         ans = None

#         def dfs(node):
#             nonlocal count, ans
#             print(count)
#             if not naode:
#                 return

#             dfs(node.left)
#             count += 1
#             if count == k:
#                 ans = node.val
#                 return
#             dfs(node.right)
#         dfs(root)
#         return  ans

# # time complexity = O(n)
# # space complexity = O(n)
