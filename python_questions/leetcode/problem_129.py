# # Quesiton:
# 129. Sum Root to Leaf Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# # Solution:

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return []

#         res = []
#         def dfs(node,path):
#             print(path)
#             if not node.right and not node.left:
#                 res.append("".join(path + [str(node.val)]))
#                 return
#             if node.left:
#                 dfs(node.left,path + [str(node.val)])
#             if node.right:
#                 dfs(node.right,path + [str(node.val)])

#             return res

#         dfs(root,[])
#         print(res)

#         return sum(int(x) for x in res)
# # time complexity = O(n)
# # space complexity = O(n)
