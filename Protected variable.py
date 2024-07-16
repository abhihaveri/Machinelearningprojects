### Protected variable 

class Person:
    #constrctor 
    def __init__(self,name,age):
        self._name=name
        self._age=age

class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)


    # public method to use Protected variable outside defined class is shown below is only in derived case 
    def display_details(self):
        print(f"The name of the person is { self._name} and the age is {self._age}")


person1=Student("Abhishek",31)

person1.display_details()

## Best practise is use protected inised a derived variable same for private use it insidde a method never use outside classes 


