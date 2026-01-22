# # Quesiton:
# 976. Largest Perimeter Triangle
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# # Solution:


# # time complexity = O(n)class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)

#         while n > 2:
#             c = nums[n-1]
#             b = nums[n-2]
#             a = nums[n-3]

#             if  a + b > c :
#                 return a + b + c
#             else :
#                 n -= 1
#         return 0
# # space complexity = O(n)
