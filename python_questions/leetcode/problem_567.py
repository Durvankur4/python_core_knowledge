# # Quesiton:
# 567. Permutation in String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# # Solution:

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count_1 = {}
#         count_2 = {}
#         l = 0
#         if len(s1) > len(s2):
#             return False

#         for c in s1:
#             count_1[c] = count_1.get(c, 0) + 1
#         for c in range(len(s1)):
#             count_2[s2[c]] = count_2.get(s2[c], 0) + 1

#         if count_1 == count_2:
#             return True

#         for c in s2[len(s1) :]:
#             count_2[c] = count_2.get(c, 0) + 1
#             count_2[s2[l]] -= 1
#             if count_2[s2[l]] == 0:
#                 count_2.pop(s2[l])
#             l += 1
#             if count_1 == count_2:
#                 return True
#         print(count_1, count_2)
#         return False

# # time complexity = O(n)
# # space complexity = O(n)
