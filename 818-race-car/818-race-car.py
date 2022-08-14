class Solution:
    def racecar(self, target: int) -> int:
        #target*log(target)
        
        queue = deque([(0, 1)]) #[pos, velocity]
        moves = 0
        while queue:
            for _ in range(len(queue)):
                pos, vel = queue.popleft()
                
                if pos == target:
                    return moves
               
                queue.append((pos + vel, 2 * vel))
                
                #3. Only consider changing the direction of the car if one of the following conditions is true
                #   i.  The car is driving away from the target.
                #   ii. The car will pass the target in the next move.  
                if (pos + vel > target and vel > 0):
                    queue.append((pos, -1))
                
                if (pos + vel < target and vel < 0):
                    queue.append((pos, 1))
                    
            moves += 1
        
    
    #with vis, memozing state
        queue = deque([(0, 1)]) #[pos, velocity]
        vis = set()
        moves = 0
        while queue:
            for _ in range(len(queue)):
                pos, vel = queue.popleft()
                
                if pos == target:
                    return moves
               
                if (pos + vel, 2 * vel) not in vis:
                    queue.append((pos + vel, 2 * vel))
                    vis.add((pos + vel, 2 * vel))
                
                #3. Only consider changing the direction of the car if one of the following conditions is true
                #   i.  The car is driving away from the target.
                #   ii. The car will pass the target in the next move.  
                if (pos + vel > target and vel > 0 and (pos, -1) not in vis):
                    queue.append((pos, -1))
                    vis.add((pos, -1))
                
                if (pos + vel < target and vel < 0 and (pos, 1) not in vis):
                    queue.append((pos, 1))
                    vis.add((pos, 1))
                    
            moves += 1
            
            
#             To know the TC, we first need to figure out V (the number of vertices in the graph) and E (the number of edges in the graph), because we know TC of BFS is O(V + E). For this question, each vertex is a (position, speed) state, and each (position, speed) state is connected to two other states (via accelerate or reverse). Therefore E is twice of V. So the TC can be simplified as O(V).
# The number of positions is O(target) and number of speed is O(log(target)), so the number of state is O(target * log(target)) and this is the TC. If this analysis is too short to be convincing, the following is a more detailed analysis.
# The solution visits 2 * target positions which are [0, 1, 2, ..., 2 * target - 1]
# On each position you can try a number of speed and, as analysed below, this number is 2 * log2(target) + 4, at most.
# The possible speed at each position is: [1, 2, 4, ..., s] and their opposite numbers [-1, -2, ..., -s]. s is the greatest number that is less than or equal to 2 * target (because speed greater than that would send the car out of the scope that we consider) and is power of 2. So, if s is written as 2^k, then k is the integer part of log2(2 * target).
# So there are log2(target) + 2 (this is k+1, the length of [1, 2, ..., s] list) positive speeds, and hence 2 * log2(target) + 4 possible speeds. The number of (position, speed) states is: (2 * target) * (2 * log2(target) + 4) = 4 * target * log2(target) + 8 * target. This is the V (the number of vertices) of the graph we DFS on.
# So the time complexity O(V) is O(4 * target * log2(target) + 8 * target), i.e. O(target * log(target)).
# Thanks, vuluy, for your input.