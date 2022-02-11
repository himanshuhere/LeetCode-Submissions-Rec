class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #bhenchod sliding window tha ye toh, like find anagram of first in second fuckk 3 ghante de diye yaaar ques recognize nhi ho rha
        #sorting and then n^2
        #map 
        #both dint work, kuki order kharab ho rha s2 ka
        
        #hints
        # Obviously, brute force will result in TLE. Think of something else.
        # How will you check whether one string is a permutation of another string?
        # One way is to sort the string and then compare. But, Is there a better way?
        # If one string is a permutation of another string then they must one common metric. What is that?
        # Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
        # What about hash table? An array of size 26?
        
        #brute
#         s1 = sorted(s1)
        
#         m, n = len(s1), len(s2)
        
#         for i in range(0, n-m+1):
#             st = sorted(s2[i: i+m])
#             if st == s1:
#                 return True
#         return False
    
        #sliding window
        k = len(s1)
        hmap = Counter(s1)
        count = len(hmap)
        
        i, j = 0, 0
        while j < len(s2):
            if s2[j] in hmap:
                hmap[s2[j]] -= 1
                if hmap[s2[j]] == 0:
                    count -= 1
            if j-i+1 == k:
                if count == 0:
                    return True
                if s2[i] in hmap:
                    hmap[s2[i]] += 1
                    if hmap[s2[i]] == 1:
                        count += 1
                i+=1
            j+=1
        return False
        
        
        
        