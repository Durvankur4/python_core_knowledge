# # Quesiton:

# 27. Remove Element
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# # Solution:

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k
# # time complexity = O(n)
# # space complexity = O(n)
