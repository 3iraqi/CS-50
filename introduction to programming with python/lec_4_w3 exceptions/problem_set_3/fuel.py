from fractions import Fraction
"""
if, though, 
X or Y is not an integer,
X is greater than Y,
Y is 0, 
ignore all this inputs.
"""

def main():

    y = fuel()

    if 1>=y>=0:
        print("E")
    elif 99 <= y<=100:
        print("F")
    else:
        print(y,end="%")




def fuel():
    while True:
        try:
           y,z=input("Fraction: ").split('/')
           x = int(round(float(Fraction(int(y),int(z)))*100) )
           if x > 100:
               raise ValueError("Fraction must be")
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            return x



main()
