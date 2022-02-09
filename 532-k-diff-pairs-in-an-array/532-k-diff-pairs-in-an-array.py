class Solution:
    def findPairs(self, nums: List[int], k: int) -> int: 
        
            
        ans = 0
        s = Counter(nums)
        if k == 0:
            for i in s:
                if s[i] > 1:
                    ans += 1
        else:         
            for num in s:
                if num+k in s:
                    ans+=1
        return ans
        
        #same optimized
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if (k > 0 and i + k) in c or (k == 0 and c[i] > 1):
                res += 1
        return res
    
    
        #two
        nums.sort()
        ans = 0
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums)-1 and nums[j] == nums[j+1]:
                j+=1
            while i < j-1 and nums[i] + k < nums[j]:
                i+=1
            if nums[i] + k == nums[j]:
                ans +=1
            j += 1
        return ans