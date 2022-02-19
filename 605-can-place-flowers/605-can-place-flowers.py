class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        if not n:
            return True
        if len(fl) == 1:
            if n == 1 and fl[0] == 0:
                return True
            else:
                return False
            
        for i in range(len(fl)):
            if i == 0:
                if fl[i] == 0 and fl[i+1] == 0:
                    n -= 1
                    fl[i] = 1
            elif i == len(fl)-1:
                if fl[i] == 0 and fl[i-1] == 0:
                    n -= 1
                    fl[i] = 1
            else:
                if fl[i] == 0 and fl[i-1] == 0 and fl[i+1] == 0:
                    n -= 1
                    fl[i] = 1
            if n == 0:
                return True
        return True if not n else False
                