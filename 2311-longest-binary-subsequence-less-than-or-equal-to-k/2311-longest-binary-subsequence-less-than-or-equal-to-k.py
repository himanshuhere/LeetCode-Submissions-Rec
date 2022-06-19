class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #greedy
        j, zeroes  = len(s)-1, s.count("0")    
        while j >=0 and  int(s[j:], 2)<= k:
            j-=1
            
        return zeroes + s[j+1:].count("1")
        
        #me during contest, nhi chala pura
#         n = len(s)
#         if s=="0":
#             return 1

#         @lru_cache(None)
#         def f(i, b, l):
#             if i <= -1:
#                 return 0
#             if b > k:
#                 return -math.inf
#             if s[i] == '1':
#                 return max(f(i-1, b, l), 1+f(i-1, b+((2**(l))), l+1))
#             else:
#                 return 1+f(i-1, b, l+1)
        
#         return f(n-1,0,0)
        
