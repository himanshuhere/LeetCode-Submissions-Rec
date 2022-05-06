class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #brute TLE
#         while True:
#             norun = True
#             tmp = s
#             for i in range(len(s)-k+1):
#                 if len(set(s[i:i+k])) == 1:
#                     tmp = s[:i] + s[i+k:]
#                     norun = False
#             s = tmp
#             if norun:
#                 return s
            
        #stack
        st = []
        for ch in s:
            if st and st[-1][0] == ch:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([ch, 1])
        
        ans = ""
        while st:
            last = st.pop()
            ans += (last[0]*last[1])
        return ans[::-1]