# # Quesiton:

# 112. Path Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False

#         def preordersum(root,total)-> bool:
#             if not root:
#                 return False

#             total += root.val
#             if not root.left and not root.right:
#                 return total == targetSum


#             return (preordersum(root.left,total) or preordersum(root.right,total))

#         return preordersum(root,total = 0)


# # time complexity = O(n)
# # space complexity = O(n)
