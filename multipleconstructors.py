
### multiple constructors scenarios ::- 
class Animal:
    # Constructor
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0] 
        elif len(args)==2:
            self.name=args[0]
            self.species=args[1]
        elif len(args)==3:
            self.name=args[0]
            self.species=args[1]
            self.age=args[2]
    # methods 
    def make_sound(self,sound):
        print(f" the sound of {self.name} is {sound}")

dog=Animal("monkey","mammals",8)
print(dog.name)
print(dog.species)
print(dog.age)

print('************************************')
dog.make_sound("Bow wow")
