class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        ans = [str(x) for x in range(1, n+1)]
        while k-1:
            ans = self.nextPermutation(ans)
            k-=1
        return "".join(ans)
        
    def nextPermutation(self, nums):
        #1 - find smaller ele from right
        ind1 = len(nums) - 2
        while ind1 >= 0 and nums[ind1] >= nums[ind1+1]:
            ind1 -= 1
        if ind1 == -1:               #nums are in descending order, edge case
            nums.reverse()
            return nums
        
        #2 fing bigger first element than ind1
        ind2 = len(nums) - 1                
        while nums[ind2] <= nums[ind1]:
            ind2 -= 1
           
        #swap them
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1] 
        
        #reverse the numbers after ind1
        l, r = ind1+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
            
        return nums
    
        
        
        
        
        
        #  M A G I C A L  -  T I N Y   L O G I C
        
        nums = [i for i in range(1, n + 1)]         #filled nums with 1 to n
        fact = 1
        for i in range(1, n):                       # till n - 1, not n
            fact = fact * i
        
        ans = ""
        k = k - 1                                   # make 0 based indexing to 1 based
        
        while True:
            ans += str(nums[ k // fact])
            nums.pop( k // fact)
            if len(nums) == 0:
                break
            k = k % fact
            fact = fact // len(nums)
        return ans
            
        