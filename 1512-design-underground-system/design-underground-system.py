class UndergroundSystem:

    def __init__(self):
        self.journeys = {}
        self.averages = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.journeys[id] = self.Journey(id,stationName,t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        timeDif = t - self.journeys[id].t
        stations = self.journeys[id].stationName + "," + stationName

        average = self.averages.get(stations,self.Average())

        average.updateAverage(timeDif)    

        self.averages[stations] = average

        self.journeys.pop(id)    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = startStation + "," + endStation
        return self.averages[stations].getAverage()

    
    class Journey:
        def __init__(self,id: int,stationName: str,t: int):
            self.id = id
            self.stationName = stationName
            self.t = t
    
    class Average:
        def __init__(self):
            self.totalTime = 0
            self.customers = 0

        def updateAverage(self,timeDif):
            self.totalTime += timeDif
            self.customers += 1

        def getAverage(self):
            return self.totalTime / self.customers

# SC -> O(N+M)
# TC -> O(1)

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)