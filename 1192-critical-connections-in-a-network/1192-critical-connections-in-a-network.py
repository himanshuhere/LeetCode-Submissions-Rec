class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #bridges in graph 
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        #time of entry/insertion into the dfs for this nod
        
        vis = set()
        res = []
        def dfs(node, par):
            tin[node] = timer[0]
            low[node] = timer[0]
            timer[0] += 1
            
            vis.add(node)
            for k in adj[node]:
                if k == par:    continue
                if k not in vis:
                    dfs(k, node)
                    #after dfs call done
                    low[node] = min(low[node], low[k])
                    if tin[node] < low[k]:      #see mere cur node k time of ins se k ka low kam hoga ya equal hoga to k kahi se mere tak aa sakta hai, but actual me usko lower ya equal value kahi aur se mili hai jaha se rasta hai kuki gaya to mere se hai to iska k ka tin and low mere se ek jada hi hoga agar kam hai to update hua hai kahi adjacent node se means bridge imp nhi hai but agar bada hai to sale ko koi aur rasta nhi mila kato bc.
                        res.append([node, k])   #bridge
                else:   #k in vis, thus it is a cycle. Cant be bridge do only low updation here
                    low[node] = min(low[node], low[k])
        
        tin = [None]*n
        low = [None]*n
        timer = [1]
        dfs(0, -1)
        return res