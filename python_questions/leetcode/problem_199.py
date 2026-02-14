# Quesiton:
199. Binary Tree Right Side View
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]

        while q :
            lastElement = None
            qlen = len(q)

            for i in range(qlen):
                node = q.pop(0)
                if node:
                    lastElement =  node
                    q.append(node.left)
                    q.append(node.right)
            if lastElement :
                res.append(lastElement.val)
        return res
# time complexity = O(n)
# space complexity = O(n)
