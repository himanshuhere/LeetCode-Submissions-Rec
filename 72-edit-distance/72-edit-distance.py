class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
#         @lru_cache(None)
#         def f(i, j):
#             if i < 0:
#                 return j+1          #to insert 
#             if j < 0:
#                 return i+1          #to delete
#             if s1[i] == s2[j]:
#                 return f(i-1, j-1)
#             else:
#                 return 1 + min(f(i, j-1),   #insert
#                                f(i-1, j),   #delete
#                                f(i-1, j-1)) #replace
#         return f(m-1, n-1)
    
    #PLS Understand
    #If s1[i] == s2[j], 
    #then we dont need to count ay operation just move. Its lil common sense to think there movements while doing String Matching DP problem.
    
    #Else,
    #f(i, j-1) - INSERT, because hypothetically we are inserting any char ahead of i and then it is (i+1) so (i+1) matched with j, since we hypothetically inserted same char to match. Now one operation done, so we move back to i-1, j-1 as chars matches and we dont need to do any op when they matches, BUT since new char inserted ahead of i, we never really inserted it was hypotheical scene so i will be standing at there only(Hyp. i to i+1 then i-1 so at i only). So [i, j-1] + 1
    
    #f(i-1, j) - DELETE, since i and j dont match we tend to delete i, so we deleted hypothetically so we should now move to i-1, as i is deleted right. But j will be there as it only move back once it matches none else. So [i-1, j]+ 1
    
    #f(i-1, j-1) - REPLACE, since i and j dont match we have once power to make i same as j, so they matches and we both move back with one more operation count. So, [i-1, j-1] + 1
    
    #BASE CASES, for string matching DP, there can be two possible case, Either s1 gets exhausted or s2 gets exhausted. So imagin here s1 gets exh, so i==-1, and assume j is still soemwhere in s2, so we need how many operatio to make "" to "row"(example), we need to insert remaining s2 in empty string. Thus j+1 insert operations
    #Base case 2, if s2 gets exhausted so means "roc" to "", thus we need i+1 delete operation on s2 to make s1, return i+1
    #Both empty, "" "", will be covered in first base case with return as 0
        
        
        #TABULATION
        #Lets first make it 1-based indexing
#         @lru_cache(None)
#         def f(i, j):
#             if i == 0:   return j          #to insert 
#             if j == 0:   return i          #to delete
#             if s1[i-1] == s2[j-1]:
#                 return f(i-1, j-1)
#             else:
#                 return 1 + min(f(i, j-1),   #insert
#                                f(i-1, j),   #delete
#                                f(i-1, j-1)) #replace
            
#         m, n = len(s1), len(s2)
#         return f(m, n)
        
        #Tab
#         dp = [[0]*(n+1) for _ in range(m+1)]
#         for j in range(n+1):
#             dp[0][j] = j
#         for i in range(m+1):
#             dp[i][0] = i
        
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 if s1[i-1] == s2[j-1]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
#         return dp[m][n]
        
        #Space optimized
        prev = [0]*(n+1)
        cur = [0]*(n+1)
        for j in range(n+1):        #only column is filled since i if fix = 0
            prev[j] = j
        
        for i in range(1, m+1):
            cur[0] = i              #part of base case, if j=0, put i
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    cur[j] = 1 + min(cur[j-1], prev[j], prev[j-1])
            prev = copy.copy(cur)
        return prev[-1]
    
    
        #1-D array? No see we need cur[i-1] as well as prev[i-1] that means we need cur and prev rows to be present in order to make result. Like other matching algo, that has lets say only prev[i-X] or if cur thn only cur[i] then it is possible 
    