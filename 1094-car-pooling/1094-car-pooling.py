class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        m = collections.defaultdict(int)
        for p,u,v in trips:
            m[u] += p
            m[v] += -p
        A = sorted(m)
        curc = 0
        for i in A:
            curc += (m[i])
            if curc > capacity:
                return False
        return True
        
        