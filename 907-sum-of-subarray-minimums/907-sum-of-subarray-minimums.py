class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nsl, nsr = [None]*n, [None]*n
        st = []
        
        #in single loop, will calculate both see
        for i in range(n):
            #nsl
            while st and arr[st[-1]] >= arr[i]:     #only <= lagane se submit hua
                st.pop()
            nsl[i] = i - st[-1] if st else i + 1         #distance
            st.append(i)
            
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            nsr[i] = st[-1] - i if st else n - i
            st.append(i)
        
        print(nsl, nsr)
        ans = 0
        mod = int(1e9+7)
        for i in range(n):
            ans += nsl[i]*nsr[i]*arr[i]
        return ans%mod
            
        
     #creatinf monotonic increasing stack, left right in single loop. thats how they do histogram also in single loop, this is for smaller value for greater ust change sign to <. but kher in this way since some of time reverse dir push operation works for other left indices, we need to inintialize to proper value. take care of this and boom 
    #same for dulpicates use <= or >=
        #in single loop, will calculate both see
        for i in range(n):
            #nsl
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            nsl[i] = i - st[-1] if st else i + 1        #distance
            st.append(i)
            
            while st2 and arr[st2[-1]] > arr[i]:
                prev_i = st.pop()
                nsr[pre_i] = i - st[-1]         #bcs initialized rest index as n-i
            st.append(i)