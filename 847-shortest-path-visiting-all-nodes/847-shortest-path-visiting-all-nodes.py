class Solution:
    def shortestPathLength(self, graph):
        #bit masking for states as array is mutable and cant be hashed or memoized yaha nhi dfs pe kar rhe the phele wo to same isme b laga diye fir. kher
        
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        ending_mask = (1 << n) - 1                              #all 1s all visited
        q = deque([(node, 1 << node) for node in range(n)])     #1<<node, means ith bit on. means okay node
        seen = set(q)

        steps = 0
        while q:
            for _ in range(len(q)):
                node, mask = q.popleft()
                
                if mask == ending_mask:
                        return steps
                    
                for nei in graph[node]:
                    next_mask = mask | (1 << nei)       #set ith to 1, if first time well n good, if second third its fine as ques wants to visiting allowed multiple, wese b shortest be popped by BFS
                    
                    if (nei, next_mask) not in seen:
                        seen.add((nei, next_mask))
                        q.append((nei, next_mask))
            
            steps += 1
        
     
    #next_mask = mask | (1 << nei)  , if already set fine. if not set it. 
        
        
        
#         def dp(node, mask):
#             state = (node, mask)
#             if state in cache:
#                 return cache[state]
#             if mask & (mask - 1) == 0:
#                 # Base case - mask only has a single "1", which means
#                 # that only one node has been visited (the current node)
#                 return 0

#             cache[state] = float("inf") # Avoid infinite loop in recursion
#             for neighbor in graph[node]:
#                 if mask & (1 << neighbor):
#                     already_visited = 1 + dp(neighbor, mask)
#                     not_visited = 1 + dp(neighbor, mask ^ (1 << node))
#                     cache[state] = min(cache[state], already_visited, not_visited)

#             return cache[state]

#         n = len(graph)
#         ending_mask = (1 << n) - 1
#         cache = {}

#         return min(dp(node, ending_mask) for node in range(n))