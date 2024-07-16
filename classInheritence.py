## Inheritance Concepts 

## parent class 
class Car():
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def driving(self):
        print("The Car is used of Office Driving only and not for Home Driving")

### child class 
class Audi(Car):
    def __init__(self, windows, doors, enginetype,color,horsepower):
        super().__init__(windows,doors,enginetype)
        self.color=color
        self.horsepower=horsepower

    def self_driving(self,name):
        print(f"This Self Driving Car {name} is used for the Home Use and not for the Office work")


### Initialising the object 
Audiq7=Audi(5,6,"Hybrid petrol","Yellow",3500)

print(f"The Audi Q7 model details are shown below\n1) The number of window are {Audiq7.windows}\n2) The Number of doors are {Audiq7.doors}\n3) The engine_type is {Audiq7.enginetype}\n4) The color of the car is {Audiq7.color}\n5) The Horsepower of the Car is {Audiq7.horsepower}")


Audiq7.driving()
Audiq7.self_driving("Audiq7.01")

print(dir(Audiq7))

print("**** The Parent has only limited acess here as shown below")

maruthi=Car(2,4,"Kerosene")
print(f"windows {maruthi.windows}, doors are {maruthi.doors} and engine type is {maruthi.enginetype}")
maruthi.driving()   

print(dir(maruthi))