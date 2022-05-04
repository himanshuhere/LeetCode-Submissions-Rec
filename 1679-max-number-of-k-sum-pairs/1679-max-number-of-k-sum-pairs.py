class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        m = defaultdict(int)
        c = 0
        for i in nums:
            if m[k-i] > 0:
                c += 1
                m[k-i] -= 1
            else:   
                m[i] += 1
        return c
        
        
        nums.sort()
        i, j = 0, len(nums)-1
        c = 0
        while i < j:
            if nums[i]+nums[j]==k:
                i += 1
                j -= 1
                c += 1
            elif nums[i]+nums[j]<k:
                i += 1
            else:
                j -= 1
        return c