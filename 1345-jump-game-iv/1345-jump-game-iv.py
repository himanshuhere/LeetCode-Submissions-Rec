class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #its a graph modeling problem.
        #dfs with dp takes long huge calls to fid the min path. see technically we need min ump or say min path for min path we should consider BFS if we have a destinationcall like here reaching last index else dfs will check for all path before finding optimal unnecessary calls. Better model JUMP GAME 4 liek a graph of values --> index and apply BFS with initial as 0th idnex then keep checking for n-1th and return jumps you take. Options - i-1, i+1, j (that map will help you for find app j with same value)
        #map use - j where: arr[i] == arr[j] and i != j.

        
        n = len(arr)
        d = defaultdict(list)
        for i, val in enumerate(arr):
            d[val].append(i)
        
        visited = [False for _ in range(n)]
        q = [0]
        visited[0] = True
        ans = 0
        while q:
            for i in range(len(q)):
                ind = q.pop(0)
                #print(ind)
                if ind == n-1:
                    return ans
                if ind + 1 < n and visited[ind+1] == False:
                    visited[ind+1] = True
                    q.append(ind+1)
                if ind - 1 > 0 and visited[ind-1] == False:
                    visited[ind-1] = True
                    q.append(ind-1)
                for nei in d[arr[ind]]:
                    if visited[nei] == False:
                        visited[nei] = True
                        q.append(nei)
                del d[arr[ind]]
            ans += 1
        return -1
