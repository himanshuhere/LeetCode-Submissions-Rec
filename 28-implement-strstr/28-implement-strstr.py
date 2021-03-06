class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        text, patt = haystack, needle
        if len(patt) > len(text):
            return -1
        
#         for i in range(0, len(haystack) - len(needle) + 1):  #or i <= len(A) - len(B)
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1

        #2
        return haystack.find(needle)

        #Rabin karp
        
        m = len(patt)
        p = 13      #or any bigger
        d = 26      #depends on data space, we have only small lettes cud cover in 26

        powr=m-1
        texth = 0
        patth = 0
        for i in range(m-1, -1, -1):
            patth += ((ord(patt[i])*(d**powr))%p)      #cud have taken ord(ch)-ord('a') also
            texth += ((ord(text[i])*(d**powr))%p)
            powr-=1
        
        for i in range(len(text)-m+1):
            if patth == texth:
                if text[i:i+m] == patt:
                    return i
            else:
                if i == len(text)-m:
                    return -1
                
                texth -= ((ord(text[i])*(d**(m-1)))%p)
                texth *= d          #base shift to left one
                texth += ((ord(text[i+m])*(d**0))%p)
        return -1
            
        
        #pythonic rabin karp
        #Rabin karp
        patth = hash(patt)
        for i in range(len(text)-m+1):
            if patth == hash(text[i:i+m]):
                if text[i:i+m] == patt:
                    return i
        return -1
    
    #kmp
#         if not p:
#             return 0

#         if len(p) > len(s):
#             return -1
        
#         def build_lps(s: str) -> List[int]:
#             lps = [0] * len(s)
#             j, i = 0, 1
#             while i < len(s):
#                 if s[i] == s[j]:
#                     lps[i] = j + 1
#                     i += 1
#                     j += 1
#                 else:
#                     if j > 0:
#                         j = lps[j-1]
#                     else:
#                         i += 1

#             return lps

#         lps = build_lps(p)
#         i = j = 0
#         while i < len(s):
#             if s[i] == p[j]:
#                 i += 1
#                 j += 1
#                 if j == len(p):
#                     return i - len(p)
#             else:
#                 if j > 0:
#                     j = lps[j - 1]
#                 else:
#                     i += 1

#         return -1

        