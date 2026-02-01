# # Quesiton:
# 03. Binary Tree Zigzag Level Order Traversal
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between)

# # Solution:


# # time complexity = O(n)# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res  = []
#         q = deque([root] if root else [])
#         while q :
#             level = []

#             for i in range(len(q)):
#                 node = q.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             if len(res)%2 == 1:
#                 level.reverse()
#             res.append(level)
#         return res

# # space complexity = O(n)
