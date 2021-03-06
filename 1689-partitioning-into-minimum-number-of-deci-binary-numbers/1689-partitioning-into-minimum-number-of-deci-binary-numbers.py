class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)
    
        #at last only 1 or 0 is possible on every digit, wether 10, 11, 100, 101, 110 etc. So any number say 8 will take min 8 numbers bcs it needs 8 to make and we have 1 and 0, so min 8 1s or more 0s, so 1s total 8. Similarly if you think max digit of number will take itself number of digits to make bcs we have 1s and 0s only. thus max(n)
        
        # 1  --    9
        # 10, 11 --99
        # 100, 101, 110, 111 -- 999
        # 1000, 10001, 1100, 1101, 1110, 1111 - 9999
        # 99999
        
#         Eg. 
# 1. Consider n="9"
# => We need to add 1 for 9 times to get n
# 2. n = "4201"
# => We can add    1101
#                + 1100
#                + 1000 
#                + 1000 
#              -------
# 			     4201
# or any other combination which doesnt matter for this quesiton to get n. 

# Notice how we require atleast MAX_DIGIT number of deci-binary numbers, where MAX_DIGIT is max digit in n