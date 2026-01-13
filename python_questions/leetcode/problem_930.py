# # Quesiton:
# 930. Binary Subarrays With Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

# # Solution:
# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         curr = 0
#         dict = {0:1}
#         ans = 0
#         k =goal

#         for n in nums:
#             curr += n

#             if curr - k in dict:
#                 ans += dict[curr - k]

#             dict[curr] = dict.get(curr,0) + 1

#         return ans

# # time complexity = O(n)
# # space complexity = O(n)
