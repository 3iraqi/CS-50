import random
cards = ["jack", "queen", "king"]

def main():
    # print( random.choices(cards,k=2) ) # Sampling with replacement
    print( random.sample(cards,k=2) ) # Sampling without replacement
    
    
    
    
    


if __name__=="__main__":
    main()