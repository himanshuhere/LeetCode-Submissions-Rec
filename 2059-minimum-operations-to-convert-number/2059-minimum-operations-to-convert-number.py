class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([start])
        vis = set()
        lev = 0
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                if x == goal:
                    return lev
                if (x<0 or x>1000) or (x in vis):
                    continue
                vis.add(x)
                for e in nums:
                    q.append(x+e)
                    q.append(x-e)
                    q.append(x^e)
            lev+=1
        return -1
            