import sys

class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing Name")
        # if house not in ["sherbin","masr","egypt","cairo"]:
        #     raise ValueError("Invalid House")
        self.name=name
        self.house=house
        self.patronus=patronus
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        if self.patronus.lower() == "stag":
            return "🐴"
        elif self.patronus.lower() == "otter":
            return "🦦"
        elif self.patronus.lower() == "jack russell terrier":
            return "🐶"
        else:
            return "!!!"
  # def charm(self):
        #     match self.patronus:
        #         case "stag":
        #             return "🐴"
        #         case "Otter":
        #             return "🦦"
        #         case "Jack Russell terrier":
        #             return "🐶"
        #         case _:
        #             return "❕"
    
    

def main():
    student =get_student()
    print("Expecto Patronum!")
    print(student.charm())
    print(student)
    
    

def get_student():
    name=input("Name: ")
    house=input("House: ")
    patronus=input("Patronus: ")
    return Student(name,house,patronus)
    # try:
    # except ValueError :
        
    

if __name__ == "__main__":
    main()