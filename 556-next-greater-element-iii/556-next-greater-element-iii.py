class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        
        #BAKI NEXT PERMUTAION CODE HI HAI 
        
        ind1 = len(nums)-2
        
        #1 - find smaller ele from right
        while ind1 >= 0 and int(nums[ind1]) >= int(nums[ind1+1]):
            ind1 -= 1
        if ind1 == -1:               #nums are in descending order, edge case
            # nums.reverse()
            return -1
        
        #2 fing bigger first element that ind1
        ind2 = len(nums)-1                
        while int(nums[ind2]) <= int(nums[ind1]):
            ind2 -= 1
           
        #swap them
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1] 
        
        #reverse the numbers after ind1
        l, r = ind1+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
            
            
        ans = int("".join(nums)) 
        return ans if ans < (1<<31) else -1