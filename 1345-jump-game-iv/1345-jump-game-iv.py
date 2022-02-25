class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #its a graph modeling problem.
        #dfs with dp takes long huge calls to fid the min path. see technically we need min ump or say min path for min path we should consider BFS if we have a destinationcall like here reaching last index else dfs will check for all path before finding optimal unnecessary calls. Better model JUMP GAME 4 liek a graph of values --> index and apply BFS with initial as 0th idnex then keep checking for n-1th and return jumps you take. Options - i-1, i+1, j (that map will help you for find app j with same value)
        #map use - j where: arr[i] == arr[j] and i != j.

        
        n = len(arr)
        m = defaultdict(list)
        for i in range(n):
            m[arr[i]].append(i)
        
        vis = set()
        q = deque([0])
        vis.add(0)
        jumps = 0
        
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n-1:
                    return jumps

                nextjump = i+1
                if nextjump < n and nextjump not in vis:
                    q.append(nextjump)
                    vis.add(nextjump)

                nextjump = i-1
                if nextjump >= 0 and nextjump not in vis:
                    q.append(nextjump)
                    vis.add(nextjump)

                for j in m[arr[i]]:
                    if j not in vis:
                        q.append(j)
                        vis.add(j)
                del m[arr[i]]
                #m[arr[i]] = []
            jumps+=1 
        return -1
    
    #TWO MAJOR MISTAKES I DID:
    #1. for loop nhi lagaya to ans 3 nhi 8 arha tha fir bhi dimag nh gaya. q ke bad for ka dhyan dena hai kaha hai kaha nhi lagega
    #2. map ko blank nhi kar rha use ke bad lese unnecessary iteration ho rhe the TLE agya