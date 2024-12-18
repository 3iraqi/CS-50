"""random module  To make random events"""
import random
cards = ["jack", "queen", "king"]

def main():
    """main function"""
    random.seed(1)
    print( random.choices(cards,weights=[75,20,5],k=2) ) # Sampling with replacement.
    # weights -> the probability of each card of the list of cards.
    # print( random.sample(cards,k=2) ) # Sampling without replacement

if __name__=="__main__":
    main()
