class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n+1):
            ans += [(bin(i)[2:]).count("1")]
        return ans