class Solution:
	def findLength(self, A: List[int], B: List[int]) -> int:
        #mast bevkuf banaya mereko itne time tak, ye LCS ka upgrade hai bhai
        #Longest common substring bc array bana k confuseiya diya
		n = len(A)
		m = len(B)
		
		
        
        #Tabulation
        #Initializing first row and column with 0 (for ease i intialized everthing 0 :p)
		dp = [[0]*(m + 1) for y in range(n + 1)]
		maxi = 0
		
		#this code is a lot like longest common subsequence(only else condition is different). 
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if A[i - 1] == B[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
				else:
					dp[i][j] = 0            #jab nhi match kiya link tut gyi zero kar do turant/discontinuation
				maxi = max(maxi, dp[i][j])
		return maxi