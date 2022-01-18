class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        f = [0] + f + [0]       #but it will make copy or array to add 0s, lets handle edge cases in loop
        
        for i in range(1, len(f)-1):
            # prev = f[i-1] if i-1 >= 0 else 0
            # nxt = f[i+1] if i+1 <= len(f)-1 else 0
            
            if f[i-1] == f[i] == f[i+1] == 0:
                n -= 1
                f[i] = 1
                if n == 0:  return True
        return False
    # addinf 0 to both end is a clever move to ignore handling edge cases but its a reasonable trade off with 
        # making a copy of array while adding Os, either we cud also handle edge cases if dont want
        # to make new copy. like if i+1>len(flowerbed)?0:a[i+1] i-1<0?0:a[i-1] 