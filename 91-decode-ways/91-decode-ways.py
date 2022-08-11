class Solution:
    def numDecodings(self, s: str) -> int:
        # 62. Unique Paths
        # 70. Climbing Stairs
        # 509. Fibonacci Number
        #https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-+-DFS)
        
        #listen i dont need to return strings on count so why are you taking string to consideration, just use logic
        #no matter what one char is always choice unless it is 0, if 0 it is invalid like 0, 01, 012, 0111 so when zero comes return false (this case 0 as we are counting)
        #if 1-9, fine return 1
        #now lage hath check for 2 digit no too, why 1-9 handled, 10-26 remaining, so consider i and i+1 for second take case, and with logic to cover 26 if yes go ahead else not take this case
        
    
        n = len(s)
        @lru_cache(None)
        def f(i):
            if i == n:
                return 1
            
            if s[i] == "0":
                return 0
            
            ways = f(i+1)       #one dig
            
            if (i+1<n and (s[i] =="1" or (s[i]=="2" and s[i+1] in "0123456"))):   #two dig
                ways += f(i+2)
            #or if i + 1 < len(s) and int(s[i] + s[i + 1]) in range(10,  27):

            
            return ways
            
        return f(0)
           
#start 0, nope | anywhere in center 0 , nope | at last 0 but with 10, 20 would possible make 1
# "06" - 0
# "560" - 0
# "98098" - 0
# "0" - 0
# "01" - 0
# "10" - 1
# "100"  0
# "110"  1
# "23220"  2
# "4310"  1

#so our zero condition if s[i] == "0" is only for single char/our single jump dfs(i+1) and thats always invalid, and for two digit dfs(i+1), we jump 2 indices so for the case of 10, 20 we would not reach at zero but ahead and for case like 01, 02, 02 our two digit logic will not move ahead see s[i] == 1 or 2
                