class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #sliding window but has neg so map
        #divisible means sum/k should be 0
        #so if sum/k is some temp and that temp is map so we found one subarray
        #now depends we need count/of longest lenght etc
        
        #now see if S[0-i]%k == S[0-j]%k, then for sure S[j-i]%k==0 and this is what we want
        #Imagine S[i] = 17, S[j] = 22 and S[i]%k==S[j]%k==2 so S[j-i] = 22-17 = 5%k == 0 {k = 5}
        #start map with {0:1}
        #if remainder came out -ve, make sure to add k
        
        m = {0:1}
        res = 0
        s = 0
        for i, e in enumerate(nums):
            s += e
            rem = s%k
            if rem < 0:
                rem += k
            if rem in m:
                res += m[rem]
            m[rem] = m.get(rem, 0) + 1
        return res