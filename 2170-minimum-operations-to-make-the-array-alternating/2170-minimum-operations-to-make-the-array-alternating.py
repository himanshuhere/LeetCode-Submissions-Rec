class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #Observation is every even should be equal and every odd index should be equal.
        #Greed is to find the max freq at even and odd, thus other than those changing will be minimum.
        #but cud be max of both is equal, so look for second max freq similar
        
        h1, h2 = defaultdict(int), defaultdict(int)
        for i in range(0, len(nums)):
            if i & 1 == 0:
                h1[nums[i]] += 1
            else:
                h2[nums[i]] += 1
                    

        n = len(nums)
        
        hs1 = sorted(h1.items(), key=lambda x:x[1], reverse=True)
        hs2 = sorted(h2.items(), key=lambda x:x[1], reverse=True)
        
        for i in hs1:           #if pehle hi mil gye to badiya verna karte rho try
            for j in hs2:
                if i[0] !=j[0]:
                    return n - i[1] - j[1]
                
        return n // 2               #ye case esa hoga 1,1,1,1,1,1 all same, so better make any even odd index any number