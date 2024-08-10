class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cars = {}
        self.cars[1] = big
        self.cars[2] = medium
        self.cars[3] = small        

    def addCar(self, carType: int) -> bool:
        if carType in self.cars:
            if carType == 1 and self.cars.get(carType) > 0:
                self.cars[carType] = self.cars.get(carType) - 1
                return True
            elif carType == 2 and self.cars.get(carType) > 0:
                self.cars[carType] = self.cars.get(carType) - 1
                return True
            elif carType == 3 and self.cars.get(carType) > 0:
                self.cars[carType] = self.cars.get(carType) - 1
                return True
            else:
                return False
    
    # SC -> O(1)
    # TC -> O(1)



        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)