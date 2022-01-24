class Solution:
    def minReorder(self, n: int, conn: List[List[int]]) -> int:
        #bc it worked i was just tryig, literarrly i created two graphs g and gg, g has two way connection while gg have directed as given. i am running BFS on undirected gg but checking g and making sure to make edges to 0 back on every layer see also and run on diagram you will get
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
                        if x not in gg[k]:  #only here checking directed given else undirected
                            ans+=1
                        q.append(k)
                        vis.add(k)
        return ans
                            