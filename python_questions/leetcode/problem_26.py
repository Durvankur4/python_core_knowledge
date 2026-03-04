# # Quesiton:
# 26. Remove Duplicates from Sorted Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Custom Judge:

# # Solution:
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = 1
#         for n in range(1,len(nums)):
#             if nums[n] != nums[n-1]:
#                 nums[l] = nums[n]
#                 l+=1
#         return l

# # time complexity = O(n)
# # space complexity = O(n)
