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
            
            
            
            #The BFS is memorizing pairs of speed and positions. So the total time complexity will be the number of such pairs formed before we hit the target.
#Now, How many different positions are possible to reach to target. In worst case we, could have visited every single position in both the directions i.e. from -target to +target so the total no of positions possible are O(target).
#Now, to check total no of speeds possible we could go either 1, 2, 4, 8.. or -1, -2, -4 , -8 .. .. upto (target). because we will always reach the target with speed bounded by target position. So total no of distinct speeds are 2O(log target)
#Hence time complexity= Total distinct positions(=target) * total distinct speeds (=log(target)) = O(targetlog(target)).
#some says 2^logn