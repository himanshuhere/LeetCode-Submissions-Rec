class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        cr = Counter(a)
        cm = Counter(b)

        for i in a:
            if cr[i] > cm [i]:
                return False

        return True