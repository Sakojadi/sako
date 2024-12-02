from datetime import datetime, time, timedelta
from collections import defaultdict

class Master:
    def __init__(self, name, cost, startTime, endTime):
        self.name = name
        self.cost = cost
        self.startTime = datetime.strptime(startTime, "%H:%M").time()
        self.endTime = datetime.strptime(endTime, "%H:%M").time()
        self.earnings = 0
        self.reserved = defaultdict(list) 
    
    def reserveMaster(self, date, hour):
        self.reserved[date].append(hour)
        self.earnings += self.cost
        
    def isAvailable(self, date, hour):
        if self.startTime <= hour and hour <= self.endTime and hour not in self.reserved[date]:
            return True
        else:
            return False
        
    def getCost(self):
        return self.cost

class Barbershop:
    def __init__(self):
        self.barbers = {}
        self.history = []
        
    def addMaster(self, name, cost, startTime, endTime):
        self.barbers[name] = Master(name, cost, startTime, endTime)
        return f"Added master: {name}"
        
    def removeMaster(self, name):
        if name in self.barbers:
            self.barbers.pop(name)
            return f"Master {name} removed."
        return "No master like that T-T"
    
    def reserve(self, master, time, client):
        dt = datetime.strptime(time, "%d-%m-%y %H:%M")
        date, hour = dt.date(), dt.time()
        if self.barbers[master].isAvailable(date, hour):
            self.barbers[master].reserveMaster(date, hour)
            self.history.append((master, time, client))
            return f"Reservation confirmed for {master} at {time}."
        return f"{master} is unavailable at {time}."
        
    def getHistory_id(self, name):
        arr = []
        for i in self.history:
            if i[0] == name:
                arr.append(i)
    
    def getAvailableSpots(self, date):
        
        date = datetime.strptime(date, "%d-%m-%y").date()
        schedule = {}
        working_hours = []
        for hour in range(9, 18):
            working_hours.append(time(hour, 0))
            
        for hour in working_hours:
            available = []
            for name, master in self.barbers.items():
                if master.isAvailable(date, hour):
                    available.append(name)
                    
            if available:
                schedule[hour] = available
                
        grafik = []
        for hour, masters in schedule.items():
            grafik.append(f"{hour.strftime('%H:%M')}: {', '.join(masters)}")
        return "\n".join(grafik)

    def getKassa(self):
        kassa = 0
        for i in self.history:
            kassa+=self.barbers[i[0]].getCost()
        return kassa
    
    def getEarningsMaster(self, name):
        return self.barbers[name].earnings

    def cancelReservation(self, name, date):
        datetime1 = datetime.strptime(date, "%d-%m-%y %H:%M")
        date, hour = datetime1.date(), datetime1.time()
        self.barbers[name].reserved[date].remove(hour)
        if self.barbers[name].reserved[date] == []:
            self.barbers[name].reserved.pop(date)
        return f"Canceled"



if __name__ == "__main__":
    shop = Barbershop()
    print(shop.addMaster("Taylor", 50, "09:00", "15:00"))
    print(shop.addMaster("Anna", 60, "10:00", "17:00"))
    print(shop.addMaster("Saimon", 55, "09:00", "13:00"))
    
    print(shop.reserve("Taylor", "19-11-24 09:00", "Client1"))
    print(shop.reserve("Anna", "19-11-24 10:00", "Client2"))
    print(shop.reserve("Saimon", "19-11-24 09:00", "Client3"))
    
    print("\nAvailable spots on 19-11-24:")
    print(shop.getAvailableSpots("19-11-24"))
    
    print("\nEarnings for Taylor:")
    print(shop.getEarningsMaster("Taylor"))
    
    print("\nShop's total earnings:")
    print(shop.getKassa())
    
    print("\nCanceling reservation for Taylor on 19-11-24 09:00:")
    print(shop.cancelReservation("Taylor", "19-11-24 09:00"))
    
    print("\nAvailable spots on 19-11-24 after cancellation:")
    print(shop.getAvailableSpots("19-11-24"))
    
    print("\nHistory for Taylor:")
    print(shop.getHistory_id("Taylor"))
    
    print("\nHistory for Anna:")
    print(shop.getHistory_id("Anna"))
    
    print("\nHistory for Saimon:")
    print(shop.getHistory_id("Saimon"))
    
    print("\nRemoving master Anna:")
    print(shop.removeMaster("Anna"))
    
    print("\nAvailable spots on 19-11-24 after removing Anna:")
    print(shop.getAvailableSpots("19-11-24"))
    
    print("\nEarnings for Saimon:")
    print(shop.getEarningsMaster("Saimon"))


