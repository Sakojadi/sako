class Animals():
    def __init__(self, name, species, age, health_status):
      self.name = name
      self.species = species
      self.age = age
      self.health_status = health_status
      self.caretaker = None
    
    def assignCaretaker(self, caretaker):
      self.caretaker = caretaker
      return f"caretaker: {caretaker} for {self.name}"
    
    def updateHealth(self, status):
     self.health_status = status
     return f"updated health status for {self.name} to {status}"
    
    def __str__(self):
     return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Health: {self.health_status}, Caretaker: {self.caretaker}"
    
    
    
class Species():
    def __init__(self, name, population, endangered_status):
      self.name = name
      self.population = population
      self.endangered_status = endangered_status
    
    def updatePopulation(self, change):
      popul = self.population
      self.population +=change
      return f"updated from {popul} to {self.population}"

    
    def __str__(self):
      return f"Name: {self.name}, Population: {self.population}, Status: {self.endangered_status} "
    
class CareTaker():
    def __init__(self, name):
      self.name=  name
      self.assigned_animals = []
    
    def addAnimal(self, animal):
      self.assigned_animals.append(animal)
      return f"Assigned {animal} to {self.name}"
    
    def removeAnimal(self, animal):
      self.assigned_animals.remove(animal)
      return f"removed {animal} for {self.name}"
    
    def listAnimals(self):
      return self.assigned_animals
    
    def __str__(self):
     return f"Name: {self.name}, employee_id: {self.employee_id}, Assigned Animals: {self.assegned_animals}"

class Sanctuary():
    def __init__(self, name):
      self.name = name
      self.animals = []
      self.species_list = []
      self.caretakers = []
    
    def addAnimal(self,animal):
      self.animals.append(animal)
      return f"added animal.name to Sanctuary"
    
    def removeAnimal(self, name):
        for i in self.animals:
            if i.name == name:
                self.animals.remove(i)
        return f"removed {name}"
    
    def addSpecies(self, species):
        self.species_list.append(species)
        return f"Added {species}"
        
    def assignCaretakerToAnimal(self, animal_name, caretaker_name):
        names = {}
        for i in self.caretakers:
            names[i.name] = i
        if caretaker_name not in names:
            car = CareTaker(caretaker_name)
            self.caretakers.append(caretaker_name)
        else:
            names[caretaker_name].addAnimal(animal_name)
        for i in self.animals:
            if i.name == animal_name:
                i.assignCaretaker(caretaker_name)
        return f"Added {animal_name} to {caretaker_name}"
        
    def listAnimals(self, filter=None):
        arr = []
        if filter==None:
            for i in self.animals:
                arr.append(i.__str__())
            return "\n".join(arr)
        else:
            for i in self.animals:
                if i.health_status==filter:
                    arr.append(i.__str__())
            return "\n".join(arr)
    
    def listSpecies(self, endangered_only):
        arr= []
        if endangered_only == 'True':
            for i in self.species_list:
                if i.endangered_status == 'True':
                    arr.append(i.__str__())
            return "\n".join(arr)
        else:
            for i in self.species_list:
                arr.append(i.__str__())
            return "\n".join(arr)
    
    def listCaretaker(self):
      arr = []
      for i in self.caretakers:
          arr.append(i.__str__())
      return "\n".join(arr)
    
    def updateAnimalHealth(self,name,new_status):
      for i in self.animals:
          if i.name == name:
              old = i.health_status
              i.updateHealth(new_status)
      return f"updated helth status for {name} from {old} to {new_status}"
    
if __name__=="__main__":
    sanc = Sanctuary("WORLD")
    while True:
        menu = int(input("1. Add Animal\n2. Add Species\n3. Assign Caretaker to Animal\n4. List Animals (All/Filter by Health)\n5. Update Animal Health\n6. List Species (All/Endangered Only)\n7.List Caretakers\n8.Exit\n"))
        if menu ==1:
            name = input('Name: ')
            species = input('Species: ')
            age = input('age: ')
            health = input("Health Status: ")
            b = Animals(name, species, age, health)
            print(sanc.addAnimal(b))
        elif menu == 2:
            name = input('Name: ')
            pop = input("Population: ")
            end = input("Endangered Status: ")
            sp = Species(name,pop, end)
            print(sanc.addSpecies(sp))
        elif menu == 3:
            anim = input("Animal name: ")
            care = input("Caretaker name: ")
            print(sanc.assignCaretakerToAnimal(anim, care))
        elif menu == 4:
            fil = input("List animals by health? n/your health status: ")
            if fil =='n':
                print(sanc.listAnimals())
            else:
                print(sanc.listAnimals(fil))
        elif menu == 5:
            anim = input("Animal name: ")
            hel = input("Status: ")
            print(sanc.updateAnimalHealth(anim, hel))
        elif menu == 6:
            a = input("Endangered only? True/False: ")
            print(sanc.listSpecies(a))
        elif menu == 7:
            print(sanc.listCaretaker())
        else:  
            break