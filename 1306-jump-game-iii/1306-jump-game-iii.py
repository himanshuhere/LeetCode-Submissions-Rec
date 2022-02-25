import sys
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(i):
            if  i < 0 or i >= len(arr) or vis[i]:
                return False
            if arr[i] == 0:
                return True
            vis[i] = 1
            return dfs(i + arr[i]) or dfs(i - arr[i])

        vis = [0]*len(arr)
        return dfs(start)
    
    #2
    #iterative - as it is dfs - u need stack variation to make iter. pls understand which solution
    #are dfs so u can also try stack possibility if it comes to iter implementation req
#     stack, visited, n = [start], set(), len(arr)
        
#         while stack:
#             pos = stack.pop()
#             if arr[pos] == 0: return True
#             visited.add(pos)
#             cand1, cand2 = pos + arr[pos], pos - arr[pos]
#             if cand1 <  n and cand1 not in visited: stack.append(cand1)
#             if cand2 >= 0 and cand2 not in visited: stack.append(cand2)
                
#         return False