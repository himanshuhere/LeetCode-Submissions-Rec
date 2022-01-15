class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #its a graph modeling problem.
        #dfs with dp takes long huge calls to fid the min path. see technically we need min ump or say min path for min path we should consider BFS if we have a destinationcall like here reaching last index else dfs will check for all path before finding optimal unnecessary calls. Better model JUMP GAME 4 liek a graph of values --> index and apply BFS with initial as 0th idnex then keep checking for n-1th and return jumps you take. Options - i-1, i+1, j (that map will help you for find app j with same value)
        
        n = len(arr)
        m = defaultdict(list)
        for i in range(n):
            m[arr[i]].append(i)
        
        #dont want to revisit the same index
        visited = set()
        q = deque()
        # add the 0th node in our queue as that is our starting point
        q.append(0)
        res = 0
        
        while q:
            size = len(q)
			# Here we are currently doing as many iterations as there are nodes in the queue right now
			# The reason being that we do not want to accidentally visit nodes that were not meant to be
			# Visited right now
            for _ in range(size):
                i = q.popleft()
                # don't want to revisit the same node
                if i in visited:
                    continue
                # if we reached the end then gg, we won
                if i == n-1:
                    return res
                visited.add(i)
                
                # can we move one forward?, if we can then let's try that
                if (i+1) not in visited:
                    q.append(i+1)
                    
                # can we move one back? if we can then let's try that
                if (i-1) not in visited and (i-1) >= 0:
                    q.append(i-1)
                    

                # let's add every possible value that has the same value as the current one to our list to visit
                for k in m[arr[i]]:
                    if k in visited:
                        continue
                    q.append(k)
                # No longer need to visit this node's partner values ever again, 
                # so let's remove all of it's partner values. 
                # This also stops the partner nodes from visiting each other again
                # As that is a possibility (You visit all 100s, then when you are visiting
                # the next 100 in your graph, you have to iterate through all 100s again, 
				# that is inefficient so we empty the 100s connections)
                del m[arr[i]]       #or m[arr[i]] = []
            res += 1		
            
        # if we don't get an answer, return -1. Not needed as we are guaranteed an answer but some error checking is a best practice so why not
        return -1