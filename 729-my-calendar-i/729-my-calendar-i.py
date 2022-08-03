class MyCalendar:

    #brute workd with set, but jaha tak i know ye series sayd seg tree me hai 
    def __init__(self):
        self.bookings = set()

    def book(self, st: int, end: int) -> bool:
        if (st, end) in self.bookings:
            return False
        for u, v in self.bookings:
            if not (v<=st or end<=u):
                return False
        self.bookings.add((st, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)