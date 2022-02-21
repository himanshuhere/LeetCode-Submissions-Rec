class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #Simple algo, find the xor of all. You will get x1 xor x2. but need to separate number.
        #Just check if any of the bit is 1, (it will be because both numbers are diff, in case same it is 0 but no)
        #Now, find that 1 set bit any from right. That will tell that either of number has 0 at that place and other has 1 since 0^1 or 1^0 gives 1.
        #now segragate numbers on basis of bits and then xor them separately Boom you get the ans
        
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num
        
        #Get the last set bit
        right = 1
        while n1xn2 & right == 0:
            right = right << 1
        
        x1, x2 = 0, 0
        for num in nums:
            if num & right == 0:    #bit not set
                x1 ^= num
            else:
                x2 ^= num           #bit set
        
        return [x1, x2]
    
    #NOTE : if num & right == 1: DOSNT WORK. make sure to use != 0 or == 0 
        