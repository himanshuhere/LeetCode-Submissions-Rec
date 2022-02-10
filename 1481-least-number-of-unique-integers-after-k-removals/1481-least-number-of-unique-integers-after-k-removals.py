class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = defaultdict(int)
        for num in arr:
            dic[num] += 1
        sdic = sorted(dic.items(), key=lambda x:x[1])
        
        i=0
        for (key, val) in sdic:
            while dic[key] and k:
                dic[key] -= 1
                k-=1
            if dic[key] == 0:
                del dic[key]
            
        return len(dic)
        
        
                