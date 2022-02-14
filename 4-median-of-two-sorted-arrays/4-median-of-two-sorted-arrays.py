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
    
    
    
#     Two side notes:

# A. Since C1 and C2 can be mutually determined from each other, we can just move one of them first, then calculate the other accordingly. However, it is much more practical to move C2 (the one on the shorter array) first. The reason is that on the shorter array, all positions are possible cut locations for median, but on the longer array, the positions that are too far left or right are simply impossible for a legitimate cut. For instance, [1], [2 3 4 5 6 7 8]. Clearly the cut between 2 and 3 is impossible, because the shorter array does not have that many elements to balance out the [3 4 5 6 7 8] part if you make the cut this way. Therefore, for the longer array to be used as the basis for the first cut, a range check must be performed. It would be just easier to do it on the shorter array, which requires no checks whatsoever. Also, moving only on the shorter array gives a run-time complexity of O(log(min(N1, N2))) (edited as suggested by @baselRus)

# B. The only edge case is when a cut falls on the 0th(first) or the 2Nth(last) position. For instance, if C2 = 2N2, then R2 = A2[2*N2/2] = A2[N2], which exceeds the boundary of the array. To solve this problem, we can imagine that both A1 and A2 actually have two extra elements, INT_MAX at A[-1] and INT_MAX at A[N]. These additions don't change the result, but make the implementation easier: If any L falls out of the left boundary of the array, then L = INT_MIN, and if any R falls out of the right boundary, then R = INT_MAX.

