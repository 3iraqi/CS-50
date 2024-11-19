 
try:
        x=int(input("What's x?"))
except ValueError:
        print("x is not a number")
        
print(f"x is {x}")