import sys

class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
        # self.patronus=patronus
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("House: ")
        return cls(name,house)
  
def main():
    student =Student.get() #(name="medo",house="masr") #get_student()
    
    student.house="egypt"
    print(student)
    
    # try:
    # except:
    #     print("error:")
    
    
##------------------------------------------------------------------------------------------------------------

# def get_student():
#     name=input("Name: ")
#     house=input("House: ")
#     # patronus=input("Patronus: ")
#     return Student(name,house)
#     # try:
#     # except ValueError :
        
    

if __name__ == "__main__":
    main()
    
    
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self,name):
    #     try:
    #         if not name:
    #             raise ValueError("Missing Name")
    #     except ValueError:
    #         print("Invalid Name: Name cannot be empty")
    #     else:
    #         self._name=name
    
    
    # @property  # Getter
    # def house(self):
    #     return self._house
    
    # @house.setter
    # def house(self,house):
    #     try:
    #         if house not in ["ardghet","egypt","masr"]:
    #             raise ValueError("Invalid house")
    #     except:
    #         print("Invalid house")
    #     else:
    #         self._house=house
    
# def charm(self):
    ##     if self.patronus.lower() == "stag":
    #         return "🐴"
    #     elif self.patronus.lower() == "otter":
    #         return "🦦"
    #     elif self.patronus.lower() == "jack russell terrier":
    #         return "🐶"
    #     else:
    #         return "!!!"
            
    # def charm(self):
    #        #     match self.patronus:
    #        #         case "stag":
    #        #             return "🐴"
    #        #         case "Otter":
    #        #             return "🦦"
    #        #         case "Jack Russell terrier":
    #        #             return "🐶"
    #        #         case _:
    #        #             return "❕"
    
    

##############################################----------------------------------------------------