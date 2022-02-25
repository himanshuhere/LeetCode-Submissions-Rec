class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 ,v2 = version1.split("."), version2.split(".")
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            v1cur = v1[i] if i < len(v1) else 0
            v2cur = v2[i] if i < len(v2) else 0
            
            if int(v1cur) < int(v2cur):
                return -1
            elif int(v1cur) > int(v2cur):
                return 1
            i+=1
            j+=1
        return 0
            