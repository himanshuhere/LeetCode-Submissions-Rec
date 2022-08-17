class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        n = len(nums)
        
        return min( max(j+1, i+1), max(n-i, n-j), i+1+n-j, j+1+n-i)
    
    #left side se,
    #right side se
    #left right
    #left right
    
    #we dont know i, j kom pehle hai to isliye left right me apan ne max() laga diya, aur isliye baki do condition
    