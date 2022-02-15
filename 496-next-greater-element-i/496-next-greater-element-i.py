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
    
    #thoda confusing hai but pehle proper ngr nikal k map me nums2 dal k etc kiya then socha ku ngr array banana map me direct mapping kar dete hai ki kis element k bad kon sa arha nums2 me, then nums1 se check kare lenge