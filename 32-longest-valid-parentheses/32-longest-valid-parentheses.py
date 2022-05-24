class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #TLE/ without stack/ could use stack even used initially but see you know when there is only two chars for validation better use a pointer like count, anyways stack is alos good and same n^2 logic
#         c = 0
#         ans = 0
#         for i in range(len(s)):
#             c = 0
#             for j in range(i, len(s)):
#                 if s[j] == '(':
#                     c += 1
#                 else:
#                     c -= 1
                
#                 if c < 0:       #closings are more, break
#                     break
#                 if c == 0:
#                     ans = max(ans, j-i+1)
#         return ans
    
        #stack o(n)
        ans = 0
        st = []
        st.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(ans, i-st[-1])
        return ans

