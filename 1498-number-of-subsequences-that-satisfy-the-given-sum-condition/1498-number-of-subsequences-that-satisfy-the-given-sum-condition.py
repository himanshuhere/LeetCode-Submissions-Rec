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