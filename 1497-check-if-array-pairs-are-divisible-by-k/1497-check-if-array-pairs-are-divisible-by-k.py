class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        #o(n)/o(k)
        #Very imp ques - interview.
        #whenever about k divisible on array ele - think map and remainder logic
        
        freqm = {}
        for num in arr:
            rem = num % k
            freqm[rem] = 1 + freqm.get(rem, 0)
        
        for num in arr:
            rem = num % k
            curfreq = freqm[rem]
            
            if rem == 0:
                if curfreq & 1:
                    return False
            # elif rem == k//2    #nope, for odd it ll play wrong, 11/5=5, looking for six cant lose val
            elif 2*rem == k:
                if curfreq & 1:
                    return False
            else:
                #other_freq = freqm[k - rem]
                other_freq = freqm.get(k - rem, None)
                if curfreq != other_freq:
                    return False
        return True
                 
                