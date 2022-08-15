class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #okay i tried dfs on every node and than found max height of every childs of root. then all the roots with min height i ans. Since this is not coonneted graph we cant use visited (dry run n see) thus sol goes n^2 and got TLE. 
        #Sol was valid but not optimized. Second thing comes in my mind when i got dfs TLE is to first fo Topo dfs and find valid path but since it is a tree graph could find one single topo path(dry run). Actual ans is doing Topological sort yes but BFS one where fist we get rid of leaves i guess kahns algo or something see copy or kind of alternate. Main o(n) logic is that every tree-graph will have 1 or 2 centroids, visualize it and see yes one or two. 
        #And, surely height from centroids of tree wud be min than any other nodes and even max is fron leaf nodes.
        
        #Algo - 1. Put all nodes with adj lenght as 1 means leaf 
        #2.Do iter on queue and remove thos leaves from other connection thus others will become leaf (just prev one) keep chekcing and put in queue for next iter. Keep doing untill 2 or 1 nodes left. 
        #3. Means all leaves will be removed froma adj layer by layer and centroids will remain and thats the ans.
        #4. Thats y this ques got setup for this perticular sol so u need to know this.
        #5 See code and understand this and yes there cud be debate why 1 or 2 centroids only cuz if 3 it will make triagle and cycle so not tree(tree has uniq paths) and 4so square and so on. 
            
        
        if n == 1: return [0]
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        #add all leaves to queue
        leaves = []         #leaves = queue
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
         
        #do bfs while centroids 
        while n > 2:
            newLeaves = []
            
            #now go to all leafs
            for i in leaves:
                #pop there connection or prev attached nodes
                pre = adj[i].pop()
                
                adj[pre].remove(i)  #detached leaf
                
                if len(adj[pre]) == 1:
                    newLeaves.append(pre)
                    
            n -= len(leaves)       
            leaves = newLeaves
            
        return leaves