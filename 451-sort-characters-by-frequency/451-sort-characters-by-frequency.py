class Solution:
    def frequencySort(self, s: str) -> str:
        #lets try heap first
        m = Counter(s)
        h = []
        for k, v in m.items():
            heappush(h, (-v, k))
        res = ""
        while h:
            v, k = heappop(h)
            v = -v
            res += (k*v)
        return res
            