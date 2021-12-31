class Solution:
    def numSquares(self, n: int) -> int:
        
        #A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always break a number 
#Test case -
#Input:  n = 100
#Output: 1
#and most per sqrs will be n itself = 1^2+1^2+1^2+...1^2
    
#     #1
#         def f(i):
#             if i <= 3:
#                 return i
#             if i in m:
#                 return m[i]
            
#             mini=float('inf')
            
#             for j in range(1, int(sqrt(i))+1):   #max sq root tak usse aage nhi 
#                 if j*j > i:   break
#                 mini = min(mini, f(i - j*j))
            
#             m[i] = mini+1
#             return m[i]
        
#         m={}
        
#         a=int(sqrt(n))
#         if a*a == n:
#             return 1
        
#         return f(n)

        #2
    
        # step 1
        dp = [i for i in range(n+1)]    #thus, base conditon for 0,1,2,3 already filled
        
		# step 2
        for i in range(4, n+1):
	        j = 0
			# step 3
	        while j*j <= i:
	            dp[i] = min(dp[i], dp[i-(j*j)] + 1)
	            j += 1
        
        return dp[-1]