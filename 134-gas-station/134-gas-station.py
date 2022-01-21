class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #brute - TLE
        def brute():
            n = len(gas)
            i = 0
            while i < n:
                j = i
                tank = 0
                first = True
                while first or j%n != i:
                    if first:
                        first = False
                    tank += gas[j%n]
                    tank -= cost[j%n]
                    if tank<0:
                        break
                    j+=1
                #print(tank, i)
                if tank>=0:
                    return i
                i+=1
            return -1
        def greedy():
            total, cur = 0, 0
            start = 0

            for i in range(len(gas)):
                total += gas[i] - cost[i]
                cur += gas[i] - cost[i]
                print(total, cur)
                if cur < 0:
                    cur = 0
                    start = i + 1
                print(start)

            if total < 0:   return -1
            return start
        return greedy()
            
            