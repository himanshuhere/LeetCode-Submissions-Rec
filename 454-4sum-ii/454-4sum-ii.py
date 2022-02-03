class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #brute -(n^4)
        #one hashmap for last array m o(n^3)/o(n)
        #two size hashmap for last two arrays o(n^2)/o(n^2)
        
        #1
        hashtable = {}
        for a in nums1:
            for b in nums2 :
                hashtable[a+b] = hashtable.get(a+b, 0) + 1
                
        count = 0         
        for c in nums3 :
            for d in nums4 :
                if -(c+d) in hashtable :
                    count += hashtable[-(c+d)]
        return count
    
    
        #2 create map for arr1 and arr2 and map2 for arr3 and arrr4. look for negative in map2 and if get multiplye with current ways
        m1, m2 = defaultdict(int), defaultdict(int)
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                m1[nums1[i]+nums2[j]]+=1
                
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                m2[nums3[i]+nums4[j]]+=1
        
        count = 0
        for i in m1:
            if -i in m2:
                count += (m1[i]*m2[-i])     #ways
        return count
                
        