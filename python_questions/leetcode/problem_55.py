# # Quesiton:
# 55. Jump Game
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# # Solution:
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:

#         max_p = 0
#         for i in range(len(nums)):
#             if max_p < i:
#                 return False
#             max_p = max(max_p,i+nums[i] )
#         return True

# # time complexity = O(n)
# # space complexity = O(n)
