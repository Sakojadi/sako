from datetime import datetime,time

class Parkovka:
    def __init__(self):
        self.cars = {}
        self.history = {}
        self.cost = {"electric":0, "basic":cost}
        
    def addCar(self,id, type):
        time = datetime.now()
        self.cars[id] = self.cars.get(id, Car(id,type,time))
        
        
    def deleteCar(self, endTime):
        pass
        
    def getCost(self,startTime, endTime):
        pass
        
class Car:
    def __init__(self, id, type, startTime):
        self.id = id
        self.type = type
        self.time = startTime
        self.history = {}
        
        
        
    