class Wizard:
    def __init__(self,name):#,age,gender):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        
    ...

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house=house
        ...
    ...
        

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
        
        
wizard=Wizard("gamasa")

student=Student("samira","egy")
professor=Professor("Mohsen","ML")

print(student.name)