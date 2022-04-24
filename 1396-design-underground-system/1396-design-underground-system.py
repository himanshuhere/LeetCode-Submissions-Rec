class UndergroundSystem:

    def __init__(self):
        self.user = defaultdict(tuple)   
        self.src_dest = defaultdict(list)   

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src, t1 = self.user[id]
        self.src_dest[(src, stationName)].append(t - t1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(sum(self.src_dest[(startStation, endStation)])/len(self.src_dest[(startStation, endStation)]))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)