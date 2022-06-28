class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        deletions = 0
        prev = float('inf')
        for freq in frequencies:
            if freq >= prev:
                new_freq = max(prev - 1, 0)
                deletions += (freq - new_freq)
                prev = new_freq
            else:
                prev = freq
        return deletions
            