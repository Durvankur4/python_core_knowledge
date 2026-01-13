# # Quesiton:

# 1248. Count Number of Nice Subarrays
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.
# # Solution:

# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         curr = 0
#         freq = {0:1}
#         l =0
#         ans = 0

#         for i in range(len(nums)):
#             a = nums[i]%2
#             curr += a
#             ans += freq.get(curr-k,0)
#             freq[curr] = 1 + freq.get(curr,0)
#         return ans

# # time complexity = O(n)
# # space complexity = O(n)
