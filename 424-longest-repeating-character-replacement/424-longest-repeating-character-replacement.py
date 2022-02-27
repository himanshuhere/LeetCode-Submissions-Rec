class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #variable sliding window
        m = defaultdict(int)
        i, j = 0, 0
        ans = 0
        count = 0
        maxRepLetter = ""
        maxRepLetterCount = 0
        
        while j < len(s):
            m[s[j]] +=1 
            if m[s[j]] > maxRepLetterCount:     #keep the max occured (max(m.value()))
                maxRepLetterCount = m[s[j]]
                maxRepLetter = s[j]
            
            window = j-i+1                
            if window - maxRepLetterCount > k:
                if s[i] in m:
                    m[s[i]] -=1 
                    if s[i] == maxRepLetter:
                        maxRepLetterCount -= 1
                i += 1
            
            ans = max(ans, j-i+1)
            
            j += 1
        return ans
    
        
#         while j < len(s):
#             m[s[j]] +=1 
            
#             window = j-i+1
#             if window - max(m.values()) <= k:       #greedy
#                 ans = max(ans, j-i+1)
                
#             elif window - max(m.values()) > k:
#                 if s[i] in m:
#                     m[s[i]] -=1 
#                 i += 1
#             j += 1
#         return ans
# #window - max(m.values()), we want to long the string so we should (greed) look for replacing the least count chars in window, so that we can save more k for others, use k less and raise yuour widnow size thats y





#         #we can always make sliding widow variable to more elegant like
#     #try to shrik window first if it is long, then capture ans. if not long we wud be capturing ans only
#         while j < len(s):
#             m[s[j]] +=1 
#             window = j-i+1
#             while window - max(m.values()) > k:
#                 if s[i] in m:
#                     m[s[i]] -=1 
#                 i += 1
#             ans = max(ans, j-i+1)
#             j += 1
#         return ans
    
#     #now ques comes, how to short bet this max(m.values()), you can right using some extra variable and maintain some logc
    
    
#         maxRepLetterCount = 0
#         while j < len(s):
#             m[s[j]] +=1 
#             maxRepLetterCount = max(maxRepLetterCount, m[s[j]])
            
#             window = j-i+1
#             if window - maxRepLetterCount <= k:       #greedy
#                 ans = max(ans, j-i+1)
                
#             elif maxRepLetterCount > k:
#                 if s[i] in m:
#                     m[s[i]] -=1 
#                 i += 1
#             j += 1
#         return ans