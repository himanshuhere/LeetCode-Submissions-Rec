class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #Sorting works here because we are just finding number of possible subsequences, ideally we shouldn't sort any array for subsequences.

        mod = int(1e9+7)
        A = sorted(nums)
        l, r = 0, len(A)-1
        ans = 0
        while l <= r:
            if A[l]+A[r] > target:
                r-=1
            else:
                #ans = (ans + pow(2, r-l))%mod
                ans = (ans + pow(2, r-l))%mod
                l+=1
        return ans%mod
    
    
    #1,2,3,4,5 say target is 7 so 5+1 is good, so [12345], 12..5, and then only make 1 constant and keep coming right to left, since right will be reducing it max min sum wont exceed, so total 2^n subsets. we cant push left to right else sum will increase and exceed target. see and understand.POW is surely taking lot of time here 