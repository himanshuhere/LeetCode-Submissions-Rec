class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #I did myself
        m = collections.defaultdict(int)        #int not list else += nhi ho payega
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
        
        #apan ne map me sare points dal diye bina bhed bhav ke ki kon start hai kon end, chadna utarna sab rakha hai har point ka bas usme map me hi loop mar diye sort karke. Bas