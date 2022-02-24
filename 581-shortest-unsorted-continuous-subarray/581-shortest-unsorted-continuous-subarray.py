class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #very easy o(4n)
        n = len(nums)
        st = []
        #there might be many diff zero space ways but this problem i did for monotonic stack toh see
        #from left we ll find the first value which causing issue
        
        #from left maintain increasing monotonicity, if anywhere it breaks capture the index, make sure to let left the legftmost index only, leftmost breakpoint thus min.
        #two pointer wold have worked if find left firts and right first worked, somw like 20,22,21,4,5,3,15, left most is 22 right most is 3, but technically 20, 15 is the edges, thus check all breakpoints and keep the one close to edge
        
        left, right = math.inf, -math.inf
        
        #increaisng stack
        for i in range(len(nums)):
            while st and nums[st[-1]] > nums[i]:
                left = min(left, st.pop())      #culprit is stack top, nit current. do test case 
            st.append(i)
                
        st = [] 
        #decreasing stack
        for i in range(len(nums)-1, -1, -1):
            while st and nums[st[-1]] <nums[i]:
                right = max(right, st.pop())      #culprit is stack top, nit current. do test case 
            st.append(i)
            
        if (left == math.inf and right == -math.inf):
            return 0 
        return right-left+1