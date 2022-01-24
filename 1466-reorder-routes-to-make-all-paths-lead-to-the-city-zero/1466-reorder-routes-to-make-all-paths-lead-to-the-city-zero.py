class Solution:
    def minReorder(self, n: int, conn: List[List[int]]) -> int:
        g = defaultdict(list)
        gg = defaultdict(list)
        for u,v in conn:
            g[u].append(v)
            g[v].append(u)
            gg[u].append(v)
            
        q = deque([0])
        vis = set([0])
        ans = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                for k in g[x]:
                    if k not in vis:
                        if x not in gg[k]:
                            ans+=1
                            
                        q.append(k)
                        vis.add(k)
        return ans
                            