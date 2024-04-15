class Dog:
    def __init__(self,name):
        self.name=name
        print(name)
        
    def add_one(self,x):
        return(x+1)
   
    def bark(self): #creating an attribute
        print("bark")
d1=Dog("Bingo")#creating an instance(d1) for the class Dog
d1.bark()
print(d1.add_one(6))

