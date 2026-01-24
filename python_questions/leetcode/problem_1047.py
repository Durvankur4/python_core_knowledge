# # Quesiton:
# 1047. Remove All Adjacent Duplicates In String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.


# # Solution:
# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#         for i in s:
#             if stack and i == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return "".join(stack)


# # time complexity = O(n)
# # space complexity = O(n)
