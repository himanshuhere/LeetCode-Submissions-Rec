#pehle i did, same algo but mai second list k sare counter pe ek ek karke kam kar rha tha TLE, so what we have to do is make union of all map of substrings then make one counter ans process all of them.

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        counters = [Counter(w) for w in words2]
        #now make a universal counter by doing UNION of all substring map
        
        unicounter = defaultdict(int)
        for m in counters:
            for k in m:
                if k not in unicounter:
                    unicounter[k] = m[k]
                else:
                    if m[k] > unicounter[k]:
                        unicounter[k] = m[k]
        
        for w in words1:
            m1 = Counter(w)
            flag = False
            for k in unicounter:
                if k not in m1 or unicounter[k] > m1[k]:
                    flag = True
                    break
            if not flag:
                res.append(w)
        return res