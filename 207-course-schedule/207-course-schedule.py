#its just finding cycle in directed graph

import sys
sys.setrecursionlimit(10**6)    #imp 
g=[]
vis=[]
selfvis=[]


class Solution:
    def canFinish(self, A: int, B: List[List[int]]) -> bool:
        global vis,selfvis,g
        
        def dfs(v): #since directed parent is not needed, you wont go back to same edge
            vis[v] = True
            selfvis[v] = True

            for k in g[v]: 
                if not vis[k]: 
                    if dfs(k): 
                        return True
                elif selfvis[k] == True: 
                    return True     #cycle

            selfvis[v] = False
            return False
        
        
        vis = [0]*(A+1)
        selfvis = [0]*(A+1)
        g=[[] for i in range(A+1)]

        for edge in B:      #directed graph
            g[edge[0]].append(edge[1])

        for i in range(1,A+1):
            if vis[i]==0: 
                if dfs(i):
                    return False
        return True