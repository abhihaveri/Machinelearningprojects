from dataclasses import dataclass

@dataclass

class Person:
    name:str
    age:int
    profession:str 

Abhi=Person("Abhishek Haveri",32,'Data Analyst')
print(Abhi.name)