class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #bc mereko samjh nhi aaya kaha se dimag chalta gaya aur mene ye likh diya aur ek bar me 44/45 Test passed. sayd ek din pehle hi word ladder - 1 kiya th waha se inspiration tha
        g = defaultdict(list)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                g[routes[i][j]].append(i)
        #print(g)
        
        q = deque([source])
        vis = set()
        res = 0
        while q:
            for _ in range(len(q)):
                stop = q.popleft()
                if stop == target:
                    return res
                for bus in g[stop]:
                    if bus in vis:  continue
                    vis.add(bus)
                    for st in routes[bus]:
                        q.append(st)
            res+=1
        return -1
            