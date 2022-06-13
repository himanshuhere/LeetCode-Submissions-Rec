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

#we tend to pop stack when top value is greater or equeal ( means this is part of res and we tend to check more forward/backward) , why we pop it, becasue the most imp step of appending index on stack every time will make sure that stack will always have values in increasing order, bigger value at top, so since we r loioking for smaller value we keep popping for the greed of smaller, then if found we put it in ans and cur index in stack.
        #calculate NSR
#         def nsr():
#             s = []
#             right = [None]*len(h)
#             last = len(h)
            
#             for i in range(len(h)-1, -1, -1):
#                 while s and h[s[-1]] >= h[i]:
#                     s.pop()
#                 right[i] = s[-1] if s else last
#                 s.append(i)
#             return right
        
#                 #calculate NSR
#         def nsl():
#             s = []
#             left = [None]*len(h)
#             first = -1
#             for i in range(len(h)):
#                 while s and h[s[-1]] >= h[i]:
#                     s.pop()
#                 left[i] = s[-1] if s else first
#                 s.append(i)
#             return left
        
        
#         ans = -math.inf
#         left, right = nsl(), nsr()
#         for i in range(len(h)):
#             ans = max(ans, (right[i]-left[i]-1)*h[i])
#         return ans
    
    #3 optmimized
        def single():
            n = len(h)
            l, r = [-1]*n, [n]*n        #imp initilization
            s = []
            for i in range(n):
                while s and h[s[-1]] >= h[i]:
                    r[s.pop()] = i
                l[i] = s[-1] if s else -1
                s.append(i)
            return l, r
        
        ans = -math.inf
        left, right = single()
        for i in range(len(h)):
            ans = max(ans, (right[i]-left[i]-1)*h[i])
        return ans
                    