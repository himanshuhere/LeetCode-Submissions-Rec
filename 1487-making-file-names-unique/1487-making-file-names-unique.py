class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        #i wrote toh ofc brute hi hai TLE dega
        #but the best part is isme halka sa hi optimization karna hai see, when you look for 0, 1 2 3 then find like 4 not there so you add 4 and add 4- 0, next time say onepiece comes again for 5, will start from again 0,1,2,3,4,5 bcs m[onepiece] still have 0, what if after finding 4 we put 4 in m[onepiece], so next time we ll start for 5 not 0
        m = {}
        res = []
        for name in names:
            if name not in m:
                m[name] = 0
                res.append(name)
            else:
                k = m[name]
                new =name + '(' +str(k+1)+ ')'
                while new in m:
                    k += 1
                    new = name + '(' +str(k+1)+ ')'
                m[name] = k
                m[new] = 0
                res.append(new)
        return res