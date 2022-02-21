class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num
        
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
        