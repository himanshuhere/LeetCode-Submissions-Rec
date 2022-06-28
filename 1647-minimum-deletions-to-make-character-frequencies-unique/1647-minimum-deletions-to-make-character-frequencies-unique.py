class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        deletions = 0
        prev = float('inf')
        for freq in frequencies:
            new_freq = freq if (freq < prev) else max(prev - 1, 0)
            deletions += (freq - new_freq)
            prev = new_freq
        return deletions
            