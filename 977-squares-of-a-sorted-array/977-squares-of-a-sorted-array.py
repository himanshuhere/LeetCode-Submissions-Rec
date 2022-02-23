class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None]*n
        k = n-1
        i, j = 0, n-1
        while i <= j:
            l, r = nums[i]*nums[i], nums[j]*nums[j]
            
            if l > r:
                ans[k] = l
                i += 1
            else:
                ans[k] = r
                j -= 1
                
            k -= 1
        return ans
                
        