class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        scount = [(sum(row), i) for i, row in enumerate(mat)]
        scount.sort()
        return [i for count, i in scount][:k]