#Kahn's BFS Topo Algo - If stack ans is not filled with N return 0, has cycle. see
adj = collections.defaultdict(list)
indegree = [0]*n
q = []      #queue or list
for u,v in pr:
adj[v].append(u)
indegree[u] += 1
for i in range(len(indegree)):      #append all outer src nodes to q
if indegree[i] == 0:
q.append(i)
#while q - NO is tarah we ll need one more space to store result. Lets use a variable till its less than N
c = 0
while c < len(q):
x = q[c]      #dont pop, consider popping but dont else lost result
c += 1
for k in adj[x]:
indegree[k] -= 1
if indegree[k] == 0:
q.append(k)
return q if c==n else []
#if confusing simple use q for doing BFS and store result in ANS and  use while q