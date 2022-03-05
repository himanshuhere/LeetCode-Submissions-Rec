class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #rough copy me bahut sahi samjh ayega actually slow hai but understandable h
        #hint - says reverse graph - transpose graph and now run dfs on every ele fuckkkkk pehle ku nhi aya dimag me
        #kabhi b graph me upar ki or jana ho to hosiyar me parent store mat karo reverse karo edges ko bc, unless asked to not modify the graph shit
        
        g = defaultdict(list)
        for u, v in edges:
            g[v].append(u)
            
        def dfs(node, root):
            vis[node] = 1
            for k in g[node]:
                if vis[k]==0:
                    ans[root].add(k)
                    dfs(k, root)
        
        ans = [set() for _ in range(n)]
        for i in range(n):
            vis=[0]*n
            dfs(i, i)
        return [sorted(row) for row in ans]
    
    
    #see the contest time wala intuitive 
    def contesttime():
        # Build graph and compute in-degree for each node;
        # Use topological for the first time to get the direct parent of each node;
        # Use topological for the second time to get all ancestors of the direct parent of each node;
            #need direct ancestor plus unke b ancestor, either go kahn and recusive to parent or this
            g = defaultdict(list)
            ind = [0]*n
            for u , v in edges:
                g[u].append(v)
                ind[v] += 1

            q = deque()
            for i in range(n):
                if ind[i] == 0:
                    q.append(i)

            ind2 = copy.deepcopy(ind)
            q2 = copy.deepcopy(q)
            ans = [set() for _ in range(n)]

            while q:
                node = q.popleft()
                for k in g[node]:
                    ans[k].add(node)         #direct parent
                    ind[k] -= 1
                    if ind[k] == 0:
                        q.append(k)

            while q2:
                node = q2.popleft()
                for k in g[node]:
                    for p in set(ans[k]):           #set karna jaruri hai bc acccept nhi hua contest me
                        for v in ans[p]:
                            ans[k].add(v)
                    ind2[k] -= 1
                    if ind2[k] == 0:
                        q2.append(k)

            return [sorted(row) for row in ans]
        
