class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #Fuck fuck fuck missed the trick. see instead of fiding borders, find the subarray
        #since we need mini borders, neeed to find maximum subarray
        #pls remember for boundaries op you need to cut down middles just
        
        n = len(nums)
        s = sum(nums)
        
        rem = s - x
        
        if rem < 0:                     #more, cant remove nay
            return -1
        if rem == 0:                    #equal, remove all
            return n
        
        #max subarray with sliding wind
        i = 0
        tmp = 0
        elements = 0
        for j in range(len(nums)):
            tmp += nums[j]
            
            while tmp > rem:
                tmp -= nums[i]
                i += 1
            if tmp == rem:
                elements = max(elements, j-i+1)
                
        return len(nums)-elements if elements else -1
        