# `# Quesiton:
# 682. Baseball Game
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# # Solution:

# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         stack = []
#         for i in operations:
#             if i == "+":
#                 stack.append(stack[-1] + stack[-2])
#             elif i == "D":
#                 stack.append(stack[-1]*2)
#             elif i == "C":
#                 stack.pop()
#             else:
#                 stack.append(int(i))

#         return sum(stack)
# # time complexity = O(n)
# # space complexity = O(n)
`