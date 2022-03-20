class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def brute():        #i wrote
            cntr = Counter(tops)
            mxcnt, mxval = 0, -1
            for i in cntr:
                if cntr[i] > mxcnt:
                    mxcnt = cntr[i]
                    mxval = i

            cntr2 = Counter(bottoms)
            mxcnt2, mxval2 = 0, -1
            for i in cntr2:
                if cntr2[i] > mxcnt2:
                    mxcnt2 = cntr2[i]
                    mxval2 = i

            if mxcnt > mxcnt2:
                for i in range(len(tops)):
                    if tops[i] != mxval:
                        tops[i], bottoms[i] = bottoms[i], tops[i]
                f = True
                for i in range(1, len(tops)):
                    if tops[i-1]!=tops[i]:
                        f = False
                        break
                #print(mxval, tops)
                if f:
                    return len(tops)-mxcnt
            else:
                for i in range(len(tops)):
                    if bottoms[i] != mxval2:
                        tops[i], bottoms[i] = bottoms[i], tops[i]
                f = True
                for i in range(1, len(tops)):
                    if bottoms[i-1]!=bottoms[i]:
                        f = False
                        break
                #print(mxval2, bottoms, "b")
                if f:
                    return len(tops)-mxcnt2

            return -1
        
        def best():
            n = len(tops)
            cntA, cntB, cntSame = [0]*7, [0]*7, [0]*7
            
            for i in range(n):
                a, b = tops[i], bottoms[i]
                cntA[a] += 1
                cntB[b] += 1
                if a == b:
                    cntSame[a] += 1
            
            ans, minswpas = math.inf, 0
            for i in range(1, 7):
                if cntA[i] + cntB[i] - cntSame[i] == n:
                    minswaps = min(cntA[i], cntB[i]) - cntSame[i]
                    ans = min(ans, minswaps)
            return ans if ans != math.inf else -1
        
        return best()