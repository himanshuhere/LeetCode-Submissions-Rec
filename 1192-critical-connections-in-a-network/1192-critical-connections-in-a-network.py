class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #brute to remove each edges and do bfs and check is all connected - o(e+v)*e
        #Tarzan algo = only dfs cost = o(v+e)
        #bridges in graph 
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        #time of entry/insertion into the dfs for this nod
        vis = set()
        res = []
        
        def dfs(node, par):
            vis.add(node)
            tin[node] = timer[0]
            low[node] = timer[0]
            timer[0] += 1
            
            
            for k in adj[node]:
                if k == par:    continue
                if k not in vis:            #forward edge, can be bridge
                    dfs(k, node)
                    #after dfs call done
                    if tin[node] < low[k]:      #k mere se b bada h mtlb koi ancestor se conncted nhi h bridge h ye mat kato
                        res.append([node, k])   #bridge
                    
                    low[node] = min(low[node], low[k])      

                else:   #backedge, no chance of getting visited. Just update it for calc bridge at other node
                    low[node] = min(low[node], tin[k])  #check if conncted to ancestor(ancestor = means low timer)
                    #low[node] = min(low[node], low[k]) wud also work
        
        
        tin = [None]*n
        low = [None]*n
        timer = [1]
        
        dfs(0, -1)
        return res
    
    
    
    #So timer har bar increment hoga aur tin and low ko jate wakt niche tak dfs same hi fill karega. then aate wakt har node apne parent ko chorkar isliye parent k liye continue, baki adjacent ndoe se min low lelega aur khud ko update kar lega mtlb uska ki ye mere sare connection se mai inpe ye min time se kam pe nhi but uske upar ja sakta hu. so aage kabhi mera against koi pucha kon pucha ek hi to hai baap mera, ki tu mere bad gaya tha tera tin and low mere se jada hoga dikha but agar kam ya equal hua to tu kahi aur se jugad banaya h na mtlb bridge nhi hai mai kahi aur se b aa sakta hu tum tak else agar jada h to bap se hi hote huye gaya hai bridge hai ye ek, bas itna sa concept hai. mtlb bap{10/10} ---> k{11/11} then after update k took min so bap{10/10} ---> k{11/9}, mtlb no bridge critical one. kuki k bolra mai 9 k through ajaunga. m not depenedent