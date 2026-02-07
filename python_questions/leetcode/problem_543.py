# # Quesiton:
# 543. Diameter of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# # Solution:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     maxD = float("-inf")
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

#         def height(root):
#             if not root:
#                 return 0

#             left =  height(root.left)
#             right =  height(root.right)

#             diam = left + right
#             self.maxD = max(self.maxD,diam)
#             return max(left,right) + 1
#         height(root)
#         return self.maxD


# # time complexity = O(n)
# # space complexity = O(n)
