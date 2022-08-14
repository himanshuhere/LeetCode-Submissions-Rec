class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        #Idea is to simple add a till its lenght is less than B, if not then too then toh add once at back now definately you ll have your sub found. 3e can use our own method instead of sub see
        
        #own's contains method, if asked
        def isContains(s, sub):         #TLE
            i, j = 0, 0
            while i < len(s):
                j = 0
                while i < len(s) and j < len(sub) and s[i] == sub[j]:
                    j += 1
                if j == len(sub):
                    return True
            return False
        
        def isContains2(s, sub):         #Worked
            subhash = hash(sub)
            for i in range(0, len(s)-len(sub)+1):
                if subhash == hash(s[i:i+len(sub)]):
                    return True
            return False
        
        #reach that max point which is min than B, after than one more operation and we are >= B
        tmp = ""
        count = 0
        while len(tmp) < len(b):
            tmp += a
            count += 1
        
        if isContains2(tmp, b):
            return count
        if isContains2(tmp+a, b):
            return count+1
        return -1
    