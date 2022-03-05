class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
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
        