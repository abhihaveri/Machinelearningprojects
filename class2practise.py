# Good ways to write classes 
# Constructors , attributes , methods 

# Classes --Real world Entity or object
# attributes--properties of the class
# methods--functions of the class 


class Car:
    #Constructors 
    def __init__(self,wheels,windows,color,engine):
        self.wheels=wheels
        self.windows=windows
        self.color=color 
        self.engine=engine
    #Methods 
    def self_driving(self,engine):
        print("The Type of New Car is {}".format(engine))

Audi=Car(5,6,"Red","Hybrid")

print("The feautures of Audi are \nwheels:: {}\nwindows:: {}\ncolor:: {}\nengine:: {}".format(Audi.windows,Audi.wheels,Audi.color,Audi.engine))
#print(f"The Engine of the New Self driving car is {}")
Audi.self_driving("Electric N02")


