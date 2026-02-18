# # Quesiton:
# 108. Convert Sorted Array to Binary Search Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def createbst(left,right):
#             if left > right:
#                 return

#             mid = (left+right)//2

#             root = TreeNode(nums[mid])
#             root.left = createbst(left,mid-1)
#             root.right = createbst(mid+1,right)
#             return root


#         return createbst(0,len(nums)-1)
# # time complexity = O(n)
# # space complexity = O(n)
