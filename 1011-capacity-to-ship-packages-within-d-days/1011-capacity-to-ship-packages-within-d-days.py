class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        #ditto same logic and ditto same code line Allocate books to sudents
        #days = students, weights = pages everything is same
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight      #start new weight on new day not like koko resume from left
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True

        lo, hi = max(weights), sum(weights)     #max(w) if low bound, always take care of like 11 total = weigth not total = total - capacity
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo