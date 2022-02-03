class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #brute -(n^4)
        #one hashmap for last array m o(n^3)/o(n)
        #two size hashmap for last two arrays o(n^2)/o(n^2)
        
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