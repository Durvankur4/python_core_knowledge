# # Quesiton:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# # Solution:

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l = 0

#         for r in range(len(nums)):
#             if nums[r] != 0 :
#                 nums[l] , nums[r] = nums[r] , nums[l]
#                 l +=1

# # time complexity = O(n)
# # space complexity = O(n)
