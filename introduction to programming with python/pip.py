


"""
if, though, 
X or Y is not an integer,
X is greater than Y,
Y is 0, 
ignore all this inputs.
"""

# x,y= input("Enter Fraction ").split("/")

# fuel()

def fuel():
    while True:
        try:
            x,y= input("Enter Fraction ").split("/")
            fuel=round(int(x)/int(y),2)*100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return fuel
        
print(int(fuel()),end="%")