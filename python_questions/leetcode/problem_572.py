# # Quesiton:
# 572. Subtree of Another Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# # Solution:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

#         r = root
#         s = subRoot

#         if not r : return False
#         if not s : return True

#         if self.sameTree(r,s) :
#             return True

#         return (self.isSubtree(r.left,s) or self.isSubtree(r.right,s))

#     def sameTree(self,p,q) -> bool:
#             if not p and not q:
#                 return True
#             if not p or not q:
#                 return False
#             if p.val != q.val:
#                 return False
#             return (self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right))


# # time complexity = O(n)
# # space complexity = O(n)
