class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        #brute, make a var to keep counting greater elements. if bigger come update and count. now if in between any value comes even greater than current count and break, see 1st index to understand.
        #TLE
#         ans = []
#         for i in range(len(heights)-1):
#             cnt = 1
#             cur = heights[i+1]
#             for j in range(i+1, len(heights)):
#                 if cur >= heights[i]:
#                         break
#                 if heights[j] > cur:
#                     cur = heights[j]
#                     cnt += 1
                    
#             ans.append(cnt)
#         ans.append(0)
#         return ans
    
    #monotonous stack - classic best example on monotonous stack. see from every element we need to see the bigger slope that is what monotonic stack is so code is
        ans = [0]*len(heights)
        st = []
        for i in range(len(heights)-1, -1, -1):
            while st and st[-1] < heights[i]:
                ans[i]+=1
                st.pop()
            ans[i] = ans[i] + 1 if st else ans[i] + 0
            st.append(heights[i])
        return ans