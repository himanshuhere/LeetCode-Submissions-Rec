class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(0, 1)]) #[pos, velocity]
        moves = 0
        while queue:
            for _ in range(len(queue)):
                pos, vel = queue.popleft()
                
                if pos == target:
                    return moves
                
                #2. Always consider moving the car in the direction it is already going.
                #ye accel ka mtlb hamesha forward nhi h jis b dire me hai car wahi jate raho aur niche eale reverse op to bas modne k liye h isko agar codition me dal diye to gadi ruk jani hai <--/-->
                queue.append((pos + vel, 2 * vel))
                
                #3. Only consider changing the direction of the car if one of the following conditions is true
                #   i.  The car is driving away from the target.
                #   ii. The car will pass the target in the next move.  
                if (pos + vel > target and vel > 0):
                    queue.append((pos, -1))
                
                if (pos + vel < target and vel < 0):
                    queue.append((pos, 1))
                    
            moves += 1