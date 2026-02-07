# # # Quesiton:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def symm(p,q):

#             if not p and not q :
#                 return True

#             if not p or not q:
#                 return False

#             if p.val != q.val:
#                 return False

#             return symm(p.left,q.right) and symm(p.right,q.left)
#         return symm(root.right,root.left)


# # # Solution:
# 101. Symmetric Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# # # time complexity = O(n)
# # # space complexity = O(n)
