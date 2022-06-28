class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        deletions = 0
        prev = float('inf')
        for freq in frequencies:
            if freq >= prev:
                new_freq = prev - 1
                deletions += (freq - new_freq)
                prev = new_freq if new_freq>0 else prev
            else:
                prev = freq
        return deletions
    
        #if sorted, prev hamesha bada ya eq hoga, bada hai to leave and go ahead else euqal hoga to change the current freq to -1, but what if pcihe wala bada ho gya ho cur se kuki mai hi operation kar rha prev-1, so mai bina check kiya prev - 1 kar dunga, kuki socho 100, 100, 100..100, so 100, 99, 98, 97, ,....2, 100, ab 100 aya mai sidha 1 kar dunga kuki it is gurantanteed k 100 se 2 k bich ki sari val present hai kuki data sorted hai aur hum hi change lar rhe distort kar rhe aur wo prev-1 kar rhe to guarantee ye val presemt hai
            