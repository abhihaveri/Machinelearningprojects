def hello(name,age=32):
    print("Hello",name,"your are ",age,"years of Age")


#hello("Abhishek")



def hello2(*args,**kwargs):
    print(args)
    print(kwargs)

#hello2("Abhishek"," Haveri",age=32,dob=1992,nationality="Indian")
lst=list(('Abhishek','Haveri'))
dict_values={'age': 32, 'dob': 1992, 'nationality': 'Indian'}

hello2(lst,dict_values)
hello2(*lst,**dict_values)