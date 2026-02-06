# # Quesiton:
# 144. Binary Tree Preorder Traversal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []

#         def preorder(root):
#             if not root:
#                 return
#             res.append(root.val)
#             preorder(root.left)
#             preorder(root.right)
#         preorder(root)
#         return res
# # time complexity = O(n)
# # space complexity = O(n)
