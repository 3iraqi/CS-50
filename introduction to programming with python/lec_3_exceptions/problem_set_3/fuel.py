from fractions import Fraction

def main():
    
    y = fuel()
    
    if y==0:
        print("E")
    elif y==100:
        print("F")
    else:
        print(y,end="%")
    
    
    
    
def fuel():
    while True:
        try:
           x= int(float(Fraction(input("Fraction: ")))*100) 
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if x > 100:
                pass
            else:            
                return x
            
        
        
main()