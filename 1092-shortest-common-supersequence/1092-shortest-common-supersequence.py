class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        #worst case and brute bigda force is str1 + str2, but that wud not be shortest one. It has LCS twice, so remove one lcs and then you have shortest ans, isse short kuch hoga b nhi jo ans ho jara sa dimag h dry run karo do test case and see how can u use lcs in this case too, bravo aditya bhai!
        N = len(str1)
        M = len(str2)
        
        def longestCommonSubsequenceTabulation(str1, str2, n, m):
            table = [[None for x in range(m + 1)] for x in range(n + 1)]
            
            for i in range(n + 1):
                for j in range(m + 1):
                    if i == 0 or j == 0:
                        table[i][j] = 0
                    else:
                        if str1[i - 1] == str2[j - 1]:
                            table[i][j] = 1 + table[i - 1][j - 1]
                        else:
                            table[i][j] = max(table[i][j - 1],
                                              table[i - 1][j])
            return table
        
        def printSCS(str1, str2, n, m, table):
            i = n
            j = m
            res = ""
            while i > 0 and j > 0:
                if str1[i - 1] == str2[j - 1]:
                    res += str1[i - 1]
                    i -= 1
                    j -= 1
                else:
                    if table[i - 1][j] > table[i][j - 1]:
                        res += str1[i - 1]
                        i -= 1
                    else:
                        res += str2[j - 1]
                        j -= 1
            print(res)
            #only one while will run
            while i > 0:
                res += str1[i - 1]
                i -= 1
            print(res)
            while j > 0:
                res += str2[j - 1]
                j -= 1
            print(res)
            print(res[::-1])
            return res[::-1]
        
        
        dp = longestCommonSubsequenceTabulation(str1, str2, N, M)
        #return m + n - dp[-1][-1]
        #if it ask for lenght only give m + n - lcs(str1, str2, m ,n): no need to print
        # print dp
        return printSCS(str1, str2, N, M, dp)
    