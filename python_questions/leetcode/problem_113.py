# # Quesiton:

# 113. Path Sum II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         res,path = [],[]

#         def dfs(node,path,ts):
#             if node.left == None and node.right == None and ts == node.val:
#                 res.append(path + [node.val])
#                 return
#             if node.left :
#                 dfs(node.left,path+[node.val],ts-node.val)
#             if node.right :
#                 dfs(node.right,path+[node.val],ts-node.val)
#             return res

#         if not root:
#             return []
#         dfs(root,path,targetSum)
#         return res
# # time complexity = O(n)
# # space complexity = O(n)
