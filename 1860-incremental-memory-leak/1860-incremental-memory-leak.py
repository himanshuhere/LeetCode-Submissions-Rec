class Solution:
    def memLeak(self, mem1: int, mem2: int) -> List[int]:
        time = 1
        while time <= mem1 or time <= mem2:
            if mem1 >= mem2:
                mem1 -= time
            else:
                mem2 -= time
            time += 1
        return [time, mem1, mem2]