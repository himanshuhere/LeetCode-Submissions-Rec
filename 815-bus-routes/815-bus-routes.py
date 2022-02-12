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
                    if bus in vis:  continue    #if bus alrdy vis, means all stops alrdy added to q
                    vis.add(bus)
                    for st in routes[bus]:
                        q.append(st)
            res+=1
        return -1
    #res is actually no of busses travelled
    #pehle vis stops pe lagaya to 44/45 passed, then bus pe lagaya kuki ek bus me travel to dont catch it unnnecerry visist. then passed
    #actually bus ya stop kisi ka b visisted valid hai but agar dono k liye do vis bana do aur dono ko maintain karo to TC optimize ho jayegi, kher yaha bus wala vis accept hogya
    

# Since this problem doesn't have weight factor, so just BFS I is fine.

# Key Point : What is vertex and what is edge ?
# In this problem, since we need to find the min buses need to take.
# So it is a better design if we set bus as the vertex and set stops as edges.
# The graph might look a little bit weird, but then I can easily use BFS to generate bus.

# Then, the problem is transforming to:
# Find the min jumps from any Vertex(bus) which has an Edge of source edge(source stop) to any Vertex(bus) which has an Edge of target edge(target stop).

            