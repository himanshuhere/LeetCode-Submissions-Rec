class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #just create NGR for nums2
        #ngr = [-1]*len(nums2)      #will use map directly instead
        st = []
        
        dic = defaultdict(int)
        
        for i in range(len(nums2)-1, -1, -1):                
            while st and nums2[st[-1]] < nums2[i]:
                st.pop()
            dic[nums2[i]] = nums2[st[-1]] if st else -1
            st.append(i)
        
        #now map nums1 to nums2 direct like direct
        return [dic[nums1[i]] for i in range(len(nums1))]