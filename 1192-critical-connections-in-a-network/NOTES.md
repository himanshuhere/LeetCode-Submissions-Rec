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
if k == par:    continue
if k not in vis:
dfs(k, node)
#after dfs call done
low[node] = min(low[node], low[k])
if tin[node] < low[k]:      #see mere cur node k time of ins se k ka low kam hoga ya equal hoga to k kahi se mere tak aa sakta hai, but actual me usko lower ya equal value kahi aur se mili hai jaha se rasta hai kuki gaya to mere se hai to iska k ka tin and low mere se ek jada hi hoga agar kam hai to update hua hai kahi adjacent node se means bridge imp nhi hai but agar bada hai to sale ko koi aur rasta nhi mila kato bc.
res.append([node, k])   #bridge
else:   #k in vis, thus it is a cycle. Cant be bridge do only low updation here
low[node] = min(low[node], low[k])
tin = [None]*n
low = [None]*n
timer = [1]
dfs(0, -1)
return res
#So timer har bar increment hoga aur tin and low ko jate wakt niche tak dfs same hi fill karega. then aate wakt har node apne parent ko chorkar isliye parent k liye continue, baki adjacent ndoe se min low lelega aur khud ko update kar lega mtlb uska ki ye mere sare connection se mai inpe ye min time se kam pe nhi but uske upar ja sakta hu. so aage kabhi mera against koi pucha kon pucha ek hi to hai baap mera, ki tu mere bad gaya tha tera tin and low mere se jada hoga dikha but agar kam ya equal hua to tu kahi aur se jugad banaya h na mtlb bridge nhi hai mai kahi aur se b aa sakta hu tum tak else agar jada h to bap se hi hote huye gaya hai bridge hai ye ek, bas itna sa concept hai. mtlb bap{10/10} ---> k{11/11} then after update k took min so bap{10/10} ---> k{11/9}, mtlb no bridge critical one. kuki k bolra mai 9 k through ajaunga. m not depenedent