# # Quesiton:

# 404. Sum of Left Leaves
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
# # Solution:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#         res = []
#         def dfs(node):
#             if node == None:
#                 return 0
#             if not node.left and not node.right:
#                 return node.val
#             if node.left:
#                 res.append(dfs(node.left))
#             if node.right:
#                 dfs(node.right)
#         dfs(root)
#         print(res)
#         return sum(x for x in res if x is not None)

# # time complexity = O(n)
# # space complexity = O(n)
