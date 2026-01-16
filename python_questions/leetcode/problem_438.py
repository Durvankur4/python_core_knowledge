# # Quesiton:
# 438. Find All Anagrams in a String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# # Solution:

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         dict_1 = {}
#         dict_2 = Counter(p)
#         l = 0
#         ans = []

#         if len(p)>len(s):
#             return ans

#         for r in range(len(p)):
#             dict_1[s[r]] = dict_1.get(s[r],0)+1

#         if dict_1 == dict_2:
#             ans.append(0)

#         for r in range(len(p),len(s)):
#             dict_1[s[r]] = dict_1.get(s[r],0)+1

#             while r-l+1 > len(p):
#                 dict_1[s[l]] -= 1
#                 if dict_1[s[l]] == 0 :
#                     dict_1.pop(s[l])
#                 l+=1
#                 if dict_1 == dict_2:
#                     ans.append(l)
#         return ans
# # time complexity = O(n)
# # space complexity = O(n)
