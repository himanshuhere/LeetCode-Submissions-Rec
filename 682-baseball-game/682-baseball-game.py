class Solution:
    def calPoints(self, ops: List[str]) -> int:
        p = []
        for ch in ops:
            if ch == '+':
                p.append(p[-1] + p[-2])
            elif ch == 'D':
                p.append(2 * p[-1])
            elif ch == 'C':
                p.pop()
            else:
                p.append(int(ch))
        return sum(p)
                