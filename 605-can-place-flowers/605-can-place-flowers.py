class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        f = [0] + f + [0]       #but it will make copy or array to add 0s, lets handle edge cases in loop
        
        for i in range(1, len(f)-1):
            prev = f[i-1] if i-1 >= 0 else 0
            nxt = f[i+1] if i+1 <= len(f)-1 else 0
            
            if prev == f[i] == nxt == 0:
                n -= 1
                f[i] = 1
                if n == 0:  return True
        return False