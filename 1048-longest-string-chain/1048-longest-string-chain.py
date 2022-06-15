class Solution:
    def longestStrChain(self, nums: List[str]) -> int:
        #pure LIS  see from #300
        
        def comp(s1, s2):
            if len(s1) != len(s2)+1:
                return False
            
            i, j = 0, 0
            while i < len(s1):
                if j < len(s2) and s1[i] == s2[j]:
                    i += 1 
                    j += 1
                else:
                    i += 1
                    
            return i==len(s1) and j==len(s2)
            
        
        nums.sort(key=len)          #IMP - len wise sort krne ka hai re abababa
        n = len(nums)
        ans = [1]*n         #eveyone make 1 LIS
        for i in range(n):
            for j in range(i):
                if comp(nums[i], nums[j]):
                    ans[i] = max(ans[i], 1+ans[j])
        return max(ans)
        
        
        
        
        
        #if needs print then this
        n = len(nums)
        ans = [1]*n         
        hash_ = [i for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                #if nums[i] > nums[j]:
                if comp(nums[i], nums[j]):
                    if ans[j] + 1 > ans[i]:
                        ans[i] = ans[j]+1
                        hash_[i] = j
        
        lis = []
        lastind_ = ans.index(max(ans))
        lis.append(nums[lastind_])
        
        while hash_[lastind_] != lastind_:
            lastind_ = hash_[lastind_]
            lis.append(nums[lastind_])
            
        return lis[::-1]