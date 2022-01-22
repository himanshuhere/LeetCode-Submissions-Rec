class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        #ques is very good if you think and visualize it properly. see first of all after analyzing i got to know that we dont need to maintain alice bob state yes no need only n param is enought i will tell how, because two base case for n, n==1(Alice wins) and n==0(Alice loses) are already enough to make more bigger results. now see second misinterpretaion i had that alice/bob will pull max square if n is >= 4 else pull 1. So technicslly for every n, user will try from 1 ... j where j will stop if for j result is already available else at pos where sq of n is not poss, seee code you eill get this
        #ex, n=5 --> next calls = n= 1, 4
        #n=15, ---> n = 1, 4, 9
        #yes
        
#         @lru_cache(None)
#         def f(n):
#             if n == 0:
#                 return False
#             if n == 1:
#                 return True
            
#             j = 1
#             while j*j <= n:
#                 if f(n - j*j) == False:   #Bob won there so now with this one step we can make alice won
#                     return True
#                 j += 1
#             return False
        
#         return f(n)
    
    
    
        dp = [False] * (n+1)
        for i in range(1, n+1): 
            for j in range(1, int(sqrt(i))+1):
                if not dp[i-j*j]:   #Bob won there so now with this one step we can make alice won
                    dp[i] = True
                    break 
        return dp[-1]