class Solution:
    def countVowelPermutation(self, n: int) -> int:
        #smart people - this is fast as we only go to needed list in inner loop using map
        map = {
            ' ': ['a', 'e', 'i', 'o', 'u'],
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],  #may not i but else yes
            'o': ['i', 'u'],
            'u': ['a']
        }

        @lru_cache(None)
        def dp(n, last):
            if n == 0: 
                return 1          
            ans = 0
            for nxt in map[last]:                
                ans = (ans + dp(n-1, nxt)) % 1_000_000_007
            return ans
        return dp(n, ' ')
        
        
        #2 me - this is slow as we try every 5 char for all levels and decide with if
        @lru_cache(None)
        def fn(n, prev):
            if n == 0:  #if everythinh selected till here, wow 1 n len str can be made
                return 1
                
            ways = 0
            for c in ['a', 'e', 'i', 'o', 'u']:
                if prev == '' or (prev=='a' and c=='e') or (prev=='e' and (c=='a' or c=='i')) or (prev=='i' and not c=='i') or (prev=='o' and (c=='i' or c=='u')) or (prev=='u' and c=='a'):
                    ways += fn(n-1, c)
            return ways
        
        a = fn(n, '')
        return a%1_000_000_007