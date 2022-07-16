class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        #Idea is to simple add a till its lenght is less than B, if not then too then toh add once at back now definately you ll have your sub found. 3e can use our own method instead of sub see
        
        tmp = ""
        count = 0
        while len(tmp) < len(b):
            tmp += a
            count += 1
        
        if b in tmp:
            return count
        if b in tmp+a:
            return count+1
        return -1
        