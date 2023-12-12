class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.averages = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = self.Checkin(id,stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        timeDif = t - self.checkins[id].t
        stations = self.checkins[id].startStation + "," + stationName
        average = self.averages.get(stations,self.Averages())
        average.updateAverage(timeDif)
        self.averages[stations] = average

        self.checkins.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = startStation + "," + endStation
        return self.averages[stations].getAverage()


    class Checkin:
        def __init__(self,id:int ,stationName:str,t:int):
            self.id = id
            self.startStation = stationName
            self.t = t

    
    class Averages:
        def __init__(self):
            self.timeTaken = 0
            self.customers = 0

        def updateAverage(self,timeDif):
            self.timeTaken+=timeDif
            self.customers+=1
        
        def getAverage(self):
            return self.timeTaken / self.customers


        # TC -> O(1)
        # SC -> O(M + N)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)