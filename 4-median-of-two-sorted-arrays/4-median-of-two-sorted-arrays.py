class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Brute o(m+n), how?- merge/add the both arrays  then find mediam. how? if even length, then avg of two middle elements else if odd then middle
        #but for interview, log(m+n) chaiye
        
        def brute():
            merged = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            while i < len(nums1):
                merged.append(nums1[i])
                i += 1
            while j < len(nums2):
                merged.append(nums2[j])
                j += 1

            n = len(merged)
            if n & 1 == 1:
                return merged[n//2]
            else:
                return (merged[n//2-1] + merged[n//2]) / 2
        
        
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:             #thats y O(log(min(n1,n2)))
            return self.findMedianSortedArrays(nums2, nums1)
        
        inf = math.inf
        lo = 0
        hi = n1
        
        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = ((n1 + n2 + 1) // 2) - cut1
            
            l1 = -inf if cut1 == 0 else nums1[cut1 - 1]
            r1 =  inf if cut1 == n1 else nums1[cut1]
            
            
            l2 = -inf if cut2 == 0 else nums2[cut2 - 1]
            r2 =  inf if cut2 == n2 else nums2[cut2]
            
            if l1 <= r2 and l2 <= r1:                            #correct partition
                if (n1 + n2) & 1 == 0:                           #even lenght
                    return (max(l1, l2) + min(r1, r2)) / 2.0     #not floor division
                else:
                    return max(l1,l2)
                
            elif l1 > r2:                           #means reduce l1, go on left
                hi = cut1 - 1
                
            else:   #r1>l2
                lo = cut1 + 1
                
        return 0.0