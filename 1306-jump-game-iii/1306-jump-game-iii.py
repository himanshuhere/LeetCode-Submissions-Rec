class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(i):
            if  i < 0 or i >= len(arr) or vis[i]:
                return False
            if arr[i] == 0:
                return True
            vis[i] = 1
            return dfs(i + arr[i]) or dfs(i - arr[i])

        vis = [0]*len(arr)
        return dfs(start)
    
    #2
        queue = deque([start])
        visited = set()
        visited.add(start)
        
        while queue:
            u = queue.popleft()
            if arr[u] == 0:
                return True
            
            nextjump = u + arr[u]
            if nextjump < len(arr) and nextjump not in visited:
                visited.add(nextjump)
                queue.append(nextjump)

            nextjump = u - arr[u]
            if nextjump >= 0 and nextjump not in visited:
                visited.add(nextjump)
                queue.append(nextjump)
                
        return False