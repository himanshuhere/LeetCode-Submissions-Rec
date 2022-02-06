class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #two pointer approach
        #even at 0. odd at 1. move two both aage
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] & 1 == 0:    #even
                i += 2
            elif nums[j] & 1 == 1:  #odd
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i+=2
                j+=2
        return nums
    
    #cud ve done i=0, j=len-1, also but uske liye len cal karke odd even hisab laga k j ko aage piche place karna hota then j-=2 har bar baki pichli wli parity 1 jese hi karna 
        n = len(nums)-1
        i = 0
        j = n-1 if (n-1)&1==1 else n-2      #we need it odd
        
        while i < j:
            if nums[i] & 1 == 0:    #even
                i += 2
            elif nums[j] & 1 == 1:  #odd
                j -= 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i+=2
                j-=2
        return nums