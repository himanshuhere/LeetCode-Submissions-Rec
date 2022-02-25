class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #constraint -- 1 <= version1.length, version2.length <= 500 wud be coverred in parsing Int in other lang

        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        
        for i in range(n):
            rev1 = int(v1[i]) if i < len(v1) else 0     #clever right
            rev2 = int(v2[i]) if i < len(v2) else 0
            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
            else:
                continue                    #imp to understand, we will not return 0 here untill we compare all revisions
        
        return 0