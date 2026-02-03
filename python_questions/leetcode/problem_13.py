# # Quesiton:
# 13. Roman to Integer
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# # Solution:
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         symbols = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#         ans = 0

#         for idx,letter in enumerate(s):
#             if idx+1 < len(s) and symbols[s[idx+1]] > symbols[s[idx]]:
#                 ans -= symbols[s[idx]]
#             else:
#                 ans += symbols[letter]
#         return ans

# # time complexity = O(n)
# # space complexity = O(n)
