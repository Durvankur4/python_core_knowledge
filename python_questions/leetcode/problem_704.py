# # # Quesiton:

# 704. Binary Search
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
# # You must write an algorithm with O(log n) runtime complexity.
# # # Solution:

# # class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l,r=0,len(nums)-1
#         while l<=r:
#             m=(l+r)//2
#             if nums[m]==target:
#                 return m
#             elif nums[m]>target:
#                 r=m-1
#             elif nums[m]<target:
#                 l=m+1
#         return -1
# # # time complexity = O(n)
# # # space complexity = O(n)
