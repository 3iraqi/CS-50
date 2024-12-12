import  random 

dice=random.choice([1,2,3,4,5,6])
print(dice)

cards=["jack","queen","King"]
random.shuffle(cards) # Change the original order of cards and return the original shuffled 
print(cards)

print(random.randint(1,9))
