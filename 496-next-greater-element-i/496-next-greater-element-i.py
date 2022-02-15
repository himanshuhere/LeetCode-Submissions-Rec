class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #just create NGR for nums2
        ngr = [-1]*len(nums2)
        st = []
        
        m = defaultdict(int)
        
        for i in range(len(nums2)-1, -1, -1):
            m[nums2[i]] = i
                
            while st and nums2[st[-1]] < nums2[i]:
                st.pop()
            ngr[i] = nums2[st[-1]] if st else -1
            st.append(i)
        
        #now map nums1 to nums2 direct like direct
        ans = []
        for i in range(len(nums1)):
            indToNums2 = m[nums1[i]]
            ans.append(ngr[indToNums2])
        return ans