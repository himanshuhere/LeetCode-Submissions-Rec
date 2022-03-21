class Solution:
    def checkRecord(self, s: str) -> bool:
        ab, late = 0, 0
        for ch in s:
            if ch == 'A':
                ab += 1
            if ch == 'L':
                late += 1
            else:
                late = 0
            if ab >= 2 or late > 2:
                return False
        return True
            