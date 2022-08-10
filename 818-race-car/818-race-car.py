class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 1)])
        moves = 0
        while queue:
            for _ in range(len(queue)):
                pos, vel = queue.popleft()
                
                if pos == target:
                    return moves
                
                #2. Always consider moving the car in the direction it is already going.
                queue.append((pos + vel, 2 * vel))
                
                #3. Only consider changing the direction of the car if one of the following conditions is true
                #   i.  The car is driving away from the target.
                #   ii. The car will pass the target in the next move.  
                if (pos + vel > target and vel > 0):
                    queue.append((pos, -1))
                
                if (pos + vel < target and vel < 0):
                    queue.append((pos, 1))
                    
            moves += 1