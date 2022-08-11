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
            
            return ways
            
        return f(0)
                
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
                