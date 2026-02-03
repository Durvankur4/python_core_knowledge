# # Quesiton:
# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

# # Solution:
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         sett = set()
#         l = 0
#         max_s = 0
#         for i in range(len(s)):
#             while s[i] in sett:
#                 sett.remove(s[l])
#                 l += 1

#             sett.add(s[i])
#             max_s = max(max_s,i-l+1)
#         return max_s

# # time complexity = O(n)
# # space complexity = O(n)
