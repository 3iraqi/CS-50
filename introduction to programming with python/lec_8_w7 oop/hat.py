import random 

class Hat:
    houses=["masr ", "egypt", "cairo"]
    
    @classmethod
    def sort(cls,name):
        print(name,"is in",random.choice(cls.houses))



# Test the Hat class
Hat.sort("Harry")