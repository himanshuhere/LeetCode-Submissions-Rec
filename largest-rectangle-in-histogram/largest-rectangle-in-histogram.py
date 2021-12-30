class Solution:
    def largestRectangleArea(self, h):
        #brute o(n^2)
#         ans = 0
#         i = 0
#         def left(i):
#             height = h[i]
#             width=0
#             i-=1
#             while i >= 0:
#                 if h[i] < height:
#                     break
#                 width+=1
#                 i-=1
#             return width*height
        
#         def right(i):
#             height = h[i]
#             width=0
#             i+=1
#             while i < len(h):
#                 if h[i] < height:
#                     break
#                 width+=1
#                 i+=1
#             return width*height
        
#         while i < len(h):
#             l = left(i)
#             r = right(i)
#             ans = max(ans, l+r+h[i])
#             i+=1
#         return ans


        #calculate NSR
        def nsr():
            s = []
            right = [None]*len(h)
            last = len(h)
            
            for i in range(len(h)-1, -1, -1):
                if i == len(h)-1:
                    right[i] = last
                elif s and h[s[-1]] < h[i]:
                    right[i] = s[-1]
                elif s and h[s[-1]] >= h[i]:
                    while s and h[s[-1]] >= h[i]:
                        s.pop()
                    if not s:
                        right[i] = last
                    else:
                        right[i] = s[-1]
                
                s.append(i)
            return right
        
                #calculate NSR
        def nsl():
            s = []
            left = [None]*len(h)
            first = -1
            
            for i in range(len(h)):
                if i == 0:
                    left[i] = first
                elif s and h[s[-1]] < h[i]:
                    left[i] = s[-1]
                elif s and h[s[-1]] >= h[i]:
                    while s and h[s[-1]] >= h[i]:
                        s.pop()
                    if not s:
                        left[i] = first
                    else:
                        left[i] = s[-1]
                
                s.append(i)
            return left
        
        
        ans = -math.inf
        left, right = nsl(), nsr()
        for i in range(len(h)):
            ans = max(ans, (right[i]-left[i]-1)*h[i])
        return ans
                    