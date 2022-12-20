class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            vis[node] = True
            for k in g[node]:
                if not vis[k]:
                    dfs(k)
            
        n = len(rooms)
        g = defaultdict(list)
        for i, ed in enumerate(rooms):
            g[i] = ed
        vis = [False]*n
        dfs(0)
        for st in vis:
            if not st:
                return False
        return True