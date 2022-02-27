class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # // this function will count totalTrips for the given time
        # // a = [1,2,3] , and at time 3 how many trips we can take? 
        # // 3/1 + 3/2 + 3/3 => 3 + 1 + 1 = 5 Trips

        def tripsTaken(sec):
            trips = 0
            for t in time:
                trips += sec//t
            return trips
        
        lo, hi = 0, int(1e14)
        while lo < hi:
            mid = (lo+hi) >> 1
            if tripsTaken(mid) >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    #highest range is based on constraint. 1 <= time[i], totalTrips <= 1e7, time and trips both can be 1e7, so consider only one input we max neeed that ele time 1e7 worst * max trips thus 1e14