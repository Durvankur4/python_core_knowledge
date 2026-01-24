# # Quesiton:
# 496. Next Greater Element I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# # Solution:

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         stack = []
#         arr = {}
#         ans = []

#         for i in range(len(nums2)-1,-1,-1):
#             #enpty
#             if not stack:
#                 stack.append(nums2[i])
#                 arr[nums2[i]] = -1
#                 continue

#             #if i greater than top change top
#             #append i and assign top as nexttop
#             while stack and stack[-1] <= nums2[i]:
#                 stack.pop()

#             if not stack:
#                 arr[nums2[i]] = -1
#             else:
#                 arr[nums2[i]] = stack[-1]

#             stack.append(nums2[i])

#         for i in nums1:
#             ans.append(arr.get(i,-1))
#         return ans
# # time complexity = O(n)
# # space complexity = O(n)
