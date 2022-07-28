class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m = {}
        tset = set()
        
        for i in range(len(s)):
            if s[i] not in m:
                #check is t[i] is new too
                if t[i] not in tset:
                    m[s[i]] = t[i]
                    tset.add(t[i])
                else:
                    return False
            else:
                if m[s[i]] != t[i]:
                    return False
        return True

#need to use set, for the case like say badc, baba. Here ba and ba are mapped to each other but when d came ( first time in s) and want to map to b, since b is already mapped to b, so false.  We need to handle t also

#         indexdict = {}
#         res = ""
        
#         for i, c in enumerate(s):
#             if c not in indexdict:
#                 indexdict[c] = i
#             res += str(indexdict[c])
#         return res
    
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t): return False
#         return self.transformString(s) == self.transformString(t)
    
#character transform is not possible. See egg, add is possible but egg, bcc is also possible.
#chars are subjective so no uss direction me mat socho.
#ascii characters k base pe nahi kuki paper, me a bhaisab p k bad arhe
#khel bas indexing ka hai

#Algo : Extract isomorphicof both the string.
#1 - use map
#2 - traverse over each char, if char is not in the map put in the map with current index in string
#3 - if char in the map, take the index value
#4 - keep making index string while doing so
#5 - both should be same, expaple 01023, 011, 01234, etc

