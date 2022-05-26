class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #Pure LIS, just instead of checking > we ll check divisibility with last element.
        #Crux or intuition - Sort the array first, since subset not subseq order dsnt matter and its fine. sorting wll help to check j and j-1 but ll be sure that j-2, j-3, etc are all divisilble becasue smalls
        
        n = len(nums)
        
        nums.sort()
        
        ans = [1]*n         
        hash_ = [i for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                #if nums[i] > nums[j]:
                if nums[i] % nums[j] == 0:
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