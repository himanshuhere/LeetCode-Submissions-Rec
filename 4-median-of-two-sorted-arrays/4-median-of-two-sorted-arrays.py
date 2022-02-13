class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Brute o(m+n), how?- merge/add the both arrays  then find mediam. how? if even length, then avg of two middle elements else if odd then middle
        #but for interview, log(m+n) chaiye
        
        
        
        
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        low=0
        high=n1
        while low<=high:
            cut1=(low+high)//2
            cut2=((n1+n2+1)//2)-cut1
            
            l1=-sys.maxsize if cut1==0 else nums1[cut1-1]
            r1=sys.maxsize if cut1==n1 else nums1[cut1]
            
            
            l2=-sys.maxsize if cut2==0 else nums2[cut2-1]
            r2=sys.maxsize if cut2==n2 else nums2[cut2]
            
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==0:
                    return (max(l1,l2)+min(r1,r2)) / 2.0    #not floor division
                else:
                    return max(l1,l2)
            elif l1>r2:
                high=cut1-1
            else:   #r1>l2
                low=cut1+1
        return 0.0