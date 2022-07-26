class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #First sort acc to position, why bcs we need adjacent cars on track bcs say 10, 20, 5, here if 5 is faster than both 10, 20 but still it ll not collide with 20 but 10 as single lane.
        #Calculate time to travel for each car from their pos to reach target
        #if aage wali car has greater ttt, they will never collide if aage wali has smaller piche wali has bigger means, pche wali speed me hai takra jayegi
        #aur same ttt aya, to destination me takra jayegi tab b count karna hai as fleet.
        #See with stack and without stack both.
        
        
        #1 Stack
        
        # pair = [(p, s) for p, s in zip(position, speed)]
        # pair.sort(reverse=True)
        # stack = []
        # for p, s in pair:  # Reverse Sorted Order
        #     stack.append((target - p) / s)          #ttt
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)
        
        #2 without stack
        carconfig = [(pos, (target-pos)/sp) for pos, sp in zip(position, speed)]    #(pos, ttt)
        carconfig.sort()
        fleet = 0
        for i in range(len(carconfig)-1, 0, -1):
            if carconfig[i-1][1] <= carconfig[i][1]:
                carconfig[i-1] = carconfig[i]
            else:
                fleet += 1
        return fleet + 1                #last leftmost fleet would not end on else thus missed counting that
            
        