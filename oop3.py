class Subjects:
    def __init__(self,paper1,paper2):
        self.paper1 =paper1
        self.paper2=paper2
    
    def exam(self,paper1,paper2):#Behaviour/function/Method-will change for every object
        print("exam is",self.paper1,self.paper2)
       
English=Subjects#Objects belonging to the class English
Somali=Subjects
print(English)#finding out the class
Somali.exam('MCQ2','Essays2')

