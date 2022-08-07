class Solution:
    def countVowelPermutation(self, n: int) -> int:
#         #smart people
#         map = {
#             ' ': ['a', 'e', 'i', 'o', 'u'],
#             'a': ['e'],
#             'e': ['a', 'i'],
#             'i': ['a', 'e', 'o', 'u'],
#             'o': ['i', 'u'],
#             'u': ['a']
#         }

#         @lru_cache(None)
#         def dp(n, last):
#             if n == 0: 
#                 return 1          
#             ans = 0
#             for nxt in map[last]:                
#                 ans = (ans + dp(n-1, nxt)) % 1_000_000_007
#             return ans
#         return dp(n, ' ')
        
        
        #me 
        @lru_cache(None)
        def fn(n, cur):
            if n == 0:
                return 1
                
            ways = 0
            for c in ['a', 'e', 'i', 'o', 'u']:
                if cur == '' or (cur=='a' and c=='e') or (cur=='e' and (c=='a' or c=='i')) or (cur=='i' and not c=='i') or (cur=='o' and (c=='i' or c=='u')) or (cur=='u' and c=='a'):
                    ways += fn(n-1, c)
            return ways
        
        a = fn(n, '')
        return a%1_000_000_007