# # Quesiton:
# 860. Lemonade Change
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# # Solution:


# # time complexity = O(n)
# # space complexity = O(n)class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         reg = {
#             20:0,
#             10:0,
#             5:0
#         }
#         i = 0
#         while i < len(bills):
#             if bills[i] == 5:
#                 reg[5]+=1
#             if bills[i] == 10:
#                 reg[10] +=1
#                 if reg[5]:
#                     reg[5] -= 1
#                 else:
#                     return False
#             if bills[i] == 20:
#                 reg[20] += 1
#                 if reg[10] and reg[5]:
#                     reg[10] -=1
#                     reg[5] -=1
#                 elif reg[5]>=3:
#                     reg[5]-=3
#                 else:
#                     return False
#             i+=1

#         return True

