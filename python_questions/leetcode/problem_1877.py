# # Quesiton:
# 1877. Minimize Maximum Pair Sum in Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

# # Solution:
# class Solution:
#     def minPairSum(self, nums: List[int]) -> int:
#         i = 0
#         j = len(nums)-1

#         nums.sort()
#         pairs=[]

#         while i<j:
#             pairs.append(nums[i]+nums[j])
#             i += 1
#             j -= 1
#         # print(pairs)
#         return max(pairs)

# # time complexity = O(n)
# # space complexity = O(n)
