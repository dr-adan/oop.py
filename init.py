class computer:
    def __init__(self,name,type):#attributes
      self.name=name
      self.type=type
    def display(self):#methods/functions
       print(self.name,self.type)

com1 = computer('Desktop','Office')
com2 = computer('Laptop','Work')
#using the attribute
com1.name
com2.type
#using the method
com1.display()
com2.display()







 
    
