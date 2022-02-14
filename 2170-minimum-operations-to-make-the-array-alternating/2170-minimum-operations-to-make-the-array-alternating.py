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
        
        hm1, hm2 = [(k, h1[k]) for k in h1.keys()],  [(k, h2[k]) for k in h2.keys()]

        hm1, hm2 = sorted(hm1, key=lambda x:x[1], reverse=True), sorted(hm2, key=lambda x:x[1], reverse=True)
        for i in hm1:
            for j in hm2:
                if i[0] !=j[0]:
                    return n - i[1] - j[1]
                
        return n // 2