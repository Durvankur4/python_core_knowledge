# # Quesiton:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def post(root):
#             if not root:
#                 return
#             post(root.left)
#             post(root.right)
#             res.append(root.val)
#         post(root)
#         return res


# # Solution:
# 145. Binary Tree Postorder Traversal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# # time complexity = O(n)
# # space complexity = O(n)
