### Private variable 

class Person:
    #constrctor 
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
# public method to use Private variable outside defined class is shown below 
    def display_details(self):
        print(f"The name of the person is { self.__name} and the age is {self.__age}")
        
person1=Person("Abhishek",31)

person1.display_details()

#print(dir(person1))
'''print(person1._Person__age) this is not a good practise'''