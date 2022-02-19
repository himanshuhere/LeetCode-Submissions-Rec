class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        #first time  worked
        def intuitive():
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
        
        
        
        #want to skip edge cases tyr this
        if n == 0:
            return True
        
        fl = [0] + fl + [0]
        for i in range(1, len(fl)-1):
            if fl[i-1] == fl[i] == fl[i+1] == 0:
                fl[i] = 1
                n -= 1
                if not n:
                    return True
        return False
