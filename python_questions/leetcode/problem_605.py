# # Quesiton:
# 605. Can Place Flowers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# # Solution:

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         fb = flowerbed
#         if n == 0:
#             return True

#         if len(flowerbed) == 1:
#             return flowerbed[0] == 0 and n <= 1

#         if (fb[0] == 0 and fb[1] == 0) :
#             fb[0] = 1
#             n -= 1
#             if n == 0 :
#                 return True
#         if fb[len(fb)-2] == 0 and fb[len(fb)-1] == 0:
#             fb[len(fb)-1] = 1
#             n -= 1
#             if n == 0 :
#                 return True


#         for i in range(0,len(fb)):
#             if n == 0:
#                 return True
#             # edge cases
#             if fb[i-1] == 0 and fb[i] == 0 and fb[i+1] == 0:
#                 fb[i] = 1
#                 n -= 1
#         print(n , fb)
#         return n == 0

# # time complexity = O(n)
# # space complexity = O(n)
