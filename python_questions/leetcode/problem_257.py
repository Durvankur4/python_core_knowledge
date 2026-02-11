# # Quesiton:
# 257. Binary Tree Paths
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# # Solution:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         ans = []
#         def dfs(root,path):
#             if root is None:
#                 return

#             if root.left is None and root.right is None:
#                 path.append(str(root.val))
#                 ans.append("->".join(path))
#                 path.pop()
#                 return


#             path.append(str(root.val))
#             dfs(root.left,path)
#             dfs(root.right,path)
#             path.pop()

#         dfs(root,[])
#         return ans


# # time complexity = O(n)
# # space complexity = O(n)
