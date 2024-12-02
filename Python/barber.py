from datetime import datetime, time, timedelta
from collections import defaultdict

class Master:
    def __init__(self, name, cost, startTime, endTime):
        self.name = name
        self.cost = cost
        self.startTime = startTime
        self.endTime = endTime
        self.earnings = 0
        self.reserved = defaultdict(list)
    
    def reserveMaster(self,time,hour):
        self.reserved[time].append(hour)
        self.earnings +=self.cost
        
    def getCost(self):
        return self.cost
        
class Barbershop:
    def __init__(self):
        self.barbers = {}
        self.history = []
        
    def addMaster(self,name,cost,startTime,endTime):
        self.barbers[name] = Master(name,cost,startTime, endTime)
        return f"added master: {name}"
        
    def removemaster(self, name):
        self.barbers.pop(name)
        return f"Master: {name} removed"
    
    def reserve(self,master, time, client):
        datetime = datetime.strptime(time, "%d-%m-%y %H:%M")
        hour = datetime.hour
        self.barbers[master].reserveMaster(time,hour)
        self.history.append((master,time,client))
        
    def getHistory_id(self,name):
        arr = []
        for i in self.history:
            if i[0] == name:
                arr.append(i)
                
    def getAvailableSpots(self,date):
        avail = {}
        datetime = datetime.strptime(date, "%d-%m-%y")
        graf = {time(9, 0):[], time(10, 0):[], time(11, 0):[], time(12, 0):[], time(13, 0):[], time(14, 0):[], time(15, 0):[], time(16, 0):[], time(17, 0):[]}
        for i in self.barbers:
            if self.barbers[i].reserved[datetime] == []:
            
    def getKassa(self):
        kassa = 0
        for i in self.history:
            kassa+=self.barbers[i[0]].getCost()
    
    def getEarningsMaster(self,name):
        return self.barbers[name].earnings

    def cancelReservation(self, name, date):
        datetime = datetime.strptime(date, "%d-%m-%y %H:%M")
        hour = datetime.hour
        datetime = datetime.strptime(date, "%d-%m-%y")
        self.barbers[name].reserved[datetime].remove(hour)
        if self.barbers[name].reserved[datetime] == []:
            self.barbers[name].reserved.pop(datetime)
            
if __name__ == "__main__":
    pass
    