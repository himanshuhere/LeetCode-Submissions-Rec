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
        
        #Same exactly
#         Maximum CPU Load (hard)

# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine. - same concept think aur kese ques ban sakte hai iss concept me kuki karne wale intervals ka logiv lagaye ge but this map with sorting is so easy 

#How intervals - just find out overlappings, at that time capacity will be added and use that

#even meetings room can also be solvable like this logic of yors